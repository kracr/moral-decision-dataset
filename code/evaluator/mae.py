import os
import json
import pandas as pd
from tqdm import tqdm
from together import Together

# Load multiple models
models = [
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "google/gemma-2-27b-it",
    "mistralai/Mistral-Small-24B-Instruct-2501",
    "Qwen/Qwen2.5-7B-Instruct-Turbo"
]

# Load case summaries from Excel
cases_df = pd.read_excel("/kaggle/working/case_scores.xlsx")

# Function to generate summarization prompt
def score_prompt(case_text):
    return f"""
    I need to build a structured dataset. Given a case, infer and extract the following ethical feature scores. 
    Return your response in valid JSON format with the following fields:

    {{
        "Severity of Consequence": float,  # Range: -1 to +1
        "Utility of Consequence": float,  # Range: -1 to +1
        "Duration of Consequence": float,  # Range: -1 to +1
        "Moral Intention": float,  # Range: -1 to +1
        "Ethical Principles": float  # Range: -1 to +1 (average of all principles upheld or violated)
    }}

    Rules:
    - If utility is negative, severity and duration should also be negative.
    - Value **human lives** over material things.
    - Value **integrity over respect > reciprocity > accountability > financial competence**.
    - Each case should be analyzed in isolation.

    Case Text: "{case_text}"
    """

# Function to query LLM and parse response
def generate_score(client, prompt, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert in ethical scoring of cases."},
                {"role": "user", "content": prompt}
            ]
        )
        generated_text = response.choices[0].message.content.strip()

        # Parse response to JSON
        try:
            generated_scores = json.loads(generated_text)
            return generated_scores
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse JSON response from model {model}. Raw response: {generated_text}")
            return None
    except Exception as e:
        print(f"Error with model {model}: {e}")
        return None

# Main function to generate scores and evaluate
def evaluate_scores(output_csv, client):
    results_table = []

    for _, row in tqdm(cases_df.iterrows(), total=len(cases_df)):
        case_id = row["Case ID"]
        case_text = row["Case Text"]

        reference_scores = {
            "Severity of Consequence": row["Severity of Consequence"],
            "Utility of Consequence": row["Utility of Consequence"],
            "Duration of Consequence": row["Duration of Consequence"],
            "Moral Intention": row["Moral Intention"],
            "Ethical Principles": row["Ethical Principles"]
        }

        for model in models:
            prompt = score_prompt(case_text)
            generated_scores = generate_score(client, prompt, model)

            # Ensure generated_scores is a dictionary
            if not isinstance(generated_scores, dict):
                generated_scores = {
                    "Severity of Consequence": "N/A",
                    "Utility of Consequence": "N/A",
                    "Duration of Consequence": "N/A",
                    "Moral Intention": "N/A",
                    "Ethical Principles": "N/A"
                }

            results_table.append({
                "Model": model,
                "Case ID": case_id,
                "Reference Severity": reference_scores["Severity of Consequence"],
                "Generated Severity": generated_scores.get("Severity of Consequence", "N/A"),
                "Reference Utility": reference_scores["Utility of Consequence"],
                "Generated Utility": generated_scores.get("Utility of Consequence", "N/A"),
                "Reference Duration": reference_scores["Duration of Consequence"],
                "Generated Duration": generated_scores.get("Duration of Consequence", "N/A"),
                "Reference Moral Intention": reference_scores["Moral Intention"],
                "Generated Moral Intention": generated_scores.get("Moral Intention", "N/A"),
                "Reference Ethical Principles": reference_scores["Ethical Principles"],
                "Generated Ethical Principles": generated_scores.get("Ethical Principles", "N/A")
            })

    # Save results as CSV
    results_df = pd.DataFrame(results_table)
    results_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

# Example usage
if __name__ == "__main__":
    os.environ['TOGETHER_API_KEY'] = "fcc7d8c4a3df1856a3ec8b074ec9cde4c4f8464bc7eb75470816e1bacdb7d041"  # Replace with your Together API Key
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
    output_csv = "/kaggle/working/evaluated_scores.csv"

    evaluate_scores(output_csv, client)
