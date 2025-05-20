#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def perform_inference(model, tokenizer, prompt):
    """
    Performs inference using the given model and prompt, setting the attention mask explicitly.
    
    Args:
        model: The pre-trained model to perform inference.
        tokenizer: The tokenizer to process the input.
        prompt (str): The formatted prompt string.
    
    Returns:
        str: The model's generated answer.
        float: Time taken for inference.
    """
    # Tokenize the input and set attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)  # Max length increased
    attention_mask = inputs['attention_mask']  # Extract attention mask
    
    # Measure inference time
    start_time = time.time()
    output = model.generate(inputs['input_ids'], attention_mask=attention_mask, max_new_tokens=200)  # Generating up to 200 new tokens
    end_time = time.time()
    
    # Decode the generated output
    inference_time = end_time - start_time
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return response, inference_time



# In[ ]:


def run_tests(models):
    """
    Runs the inference tests on the given models and dataset with different prompt styles.
    
    Args:
        models (dict): Dictionary containing the models and tokenizers.
    """
    # Loop through each model
    for model_name, (model, tokenizer) in models.items():
        print(f"\nTesting with {model_name}...\n")
        
        # Create the prompt using the function
        prompt = create_prompt()
        response, time_taken = perform_inference(model, tokenizer, prompt)
        print(f"Zero-Shot Response: {response}")
        print(f"Zero-Shot Inference Time: {time_taken:.4f} seconds\n")

# Run tests
run_tests(models)

