#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import re
from tqdm import tqdm
from together import Together

# Function to generate evaluation prompt
def evaluation_prompt(summary, features):
    return f"""
    Evaluate the correctness of the following summary and features on a scale of 0 to 5 (0 = completely wrong, 5 = perfectly correct):

    Summary: "{summary}"

    Features: {json.dumps(features, indent=4)}

    Instructions:
    - Rate the SUMMARY's accuracy on a scale of 0 to 5.
    - Rate the FEATURES' correctness on a scale of 0 to 5.
    - Return only in this format:

    Ratings:
    - Summary: [0-5]
    - Features: [0-5]

    Feedback: Provide a brief explanation of the ratings.
    """

# Function to run the evaluation agent
def run_evaluation_agent(client, prompt, model):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a strict evaluator that rates accuracy of summaries and features."},
                {"role": "user", "content": prompt}
            ]
        )
        response_text = response.choices[0].message.content.strip()
        return response_text
    except Exception as e:
        print(f"Error in API call: {e}")
        return None

# Parse the ratings from the LLM response
def parse_evaluation_response(response_text):
    if not response_text:
        return 0, 0, "No response from the model."
    try:
        # Extract ratings for summary and features
        summary_match = re.search(r"Summary:\s*\[?([0-5])\]?", response_text, re.IGNORECASE)
        features_match = re.search(r"Features:\s*\[?([0-5])\]?", response_text, re.IGNORECASE)
        feedback_match = re.search(r"Feedback:\s*(.*)", response_text, re.DOTALL)

        summary_rating = int(summary_match.group(1)) if summary_match else 0
        features_rating = int(features_match.group(1)) if features_match else 0
        feedback = feedback_match.group(1).strip() if feedback_match else "No feedback provided."

        return summary_rating, features_rating, feedback
    except Exception as e:
        print(f"Error parsing evaluation response: {e}")
        return 0, 0, "Parsing failure."

# Main function to evaluate and add results to JSON
def evaluate_json(input_json, output_json, client, llm_model):
    try:
        with open(input_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return

    updated_results = []

    for entry in tqdm(data):
        case_id = entry.get("case_id", "unknown")
        selftext = entry.get("selftext", "")
        summary = entry.get("summary", "")
        features = {key: entry[key] for key in entry if key not in ["case_id", "selftext", "summary"]}

        # Generate prompt for evaluation
        prompt = evaluation_prompt(summary, features)

        # Run evaluation agent
        evaluation_response = run_evaluation_agent(client, prompt, llm_model)

        # Parse response
        summary_rating, features_rating, feedback = parse_evaluation_response(evaluation_response)

        # Calculate overall rating
        overall_rating = (summary_rating + features_rating) / 2

        # Update entry with evaluation data
        entry["summary_rating"] = summary_rating
        entry["features_rating"] = features_rating
        entry["overall_rating"] = overall_rating
        entry["feedback"] = feedback

        updated_results.append(entry)

    # Save updated results
    try:
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(updated_results, f, indent=4, ensure_ascii=False)
        print(f"Updated JSON with evaluations saved to {output_json}")
    except Exception as e:
        print(f"Error saving output JSON: {e}")

# Example usage
if __name__ == "__main__":
    os.environ['TOGETHER_API_KEY'] = "your_api_key"  # Replace with your Together API Key
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
    llm_model = "google/gemma-2-27b-it"  # Replace with a valid Together-supported model

    input_json = "summary_and_features_flat.json"  # Input JSON file
    output_json = "evaluated_summary_and_features.json"  # Output JSON file

    evaluate_json(input_json, output_json, client, llm_model)

