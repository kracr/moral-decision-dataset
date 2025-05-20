get_ipython().system('pip install together -q')

get_ipython().system('pip install transformers')

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import time

model_paths = {
    #  "T5 Large": "t5-large",
    # "LED Base": "allenai/led-base-16384",
    # "mBART Large": "facebook/mbart-large-cc25",
    #   "DialoGPT Large": "microsoft/DialoGPT-large",
    "BART CNN Samsum": "philschmid/bart-large-cnn-samsum",
    "BLOOM 560M": "bigscience/bloom-560m"
}

# Function to load model and tokenizer
def load_model(model_name):
    print(f"Loading {model_name} model...")
    # Use AutoModelForSeq2SeqLM specifically for Pegasus, which is a seq2seq model.
    model = AutoModelForSeq2SeqLM.from_pretrained(model_paths[model_name])
    tokenizer = AutoTokenizer.from_pretrained(model_paths[model_name], use_fast=False)  # Disable fast tokenizer for Pegasus and others
    return model, tokenizer

models = {name: load_model(name) for name in model_paths}

import pandas as pd
import json

data = pd.read_json(r"practice.json")  # Use raw string with 'r'
data.head()

import torch
import time
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoModelForCausalLM,
    AutoTokenizer,
)

# Define the model paths for different architectures
model_paths = {
    "BART CNN Samsum": "philschmid/bart-large-cnn-samsum",
    "BLOOM 560M": "bigscience/bloom-560m",
    "LLaMA 2 7B": "meta-llama/Llama-2-7b-hf",
    "Gemma 7B": "google/gemma-7b",
}

# Function to load model and tokenizer dynamically
def load_model(model_name):
    print(f"Loading {model_name} model...")

    model_path = model_paths[model_name]

    # Identify if model is causal or seq2seq
    if any(x in model_path.lower() for x in ["bloom", "llama", "gemma"]):
        model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.float16, device_map="auto"
        )
    else:
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_path, torch_dtype=torch.float16, device_map="auto"
        )

    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
    return model, tokenizer

# Load all models dynamically
models = {name: load_model(name) for name in model_paths}

# Function to create the prompt
def create_prompt():
    enter_case = """For context, this happened in 2020 during the pandemic, and I never knew the names of anyone here. 
    Back in 2020, I got sick (not with covid) and I went to my doctor to get tested for strep. It was all going normal at first. 
    I walked in, put on a mask, checked in, and sat down to wait. While I was on my phone, I see a male Karen, looking to be in his 40s or 50s maybe, 
    come through the doors without a mask. The polite nurse tells him, "Sir please put a mask on," but he refuses. Instead, he starts rambling on about how he has breathing problems. 
    Again, the nurse steps in and informs this guy that breathing trouble can be a sign of covid. He then proceeds to start violently screaming at the nurse and cussing her out. 
    While all this is happening, I am sitting a short distance away. Being the only other in the room, the nurse gives me a desperate look, but socially awkward me just stayed where I was. 
    About 5 minutes later, 2 other nurses get this guy kicked out and I never saw him come back in. So, was I the jerk for doing nothing for the poor nurse?
    """
    prompt = f'Summarize the case text using this template: ' \
             f'"The active agent did action to passive agent which led to consequence. The active agent had good/bad/neutral moral intention, ' \
             f'however, the action violated ethical principle which caused an ethical issue." \n\nCase Text: "{enter_case}"'
    return prompt

# Function to run inference
def perform_inference(model, tokenizer, prompt):
    """
    Performs inference using the given model and prompt.
    """
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512).to(model.device)

    # Measure inference time
    start_time = time.time()
    output = model.generate(**inputs, max_new_tokens=200)
    end_time = time.time()

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response, end_time - start_time

# Run tests on loaded models
def run_tests(models):
    for model_name, (model, tokenizer) in models.items():
        print(f"\nTesting {model_name}...\n")
        prompt = create_prompt()
        response, time_taken = perform_inference(model, tokenizer, prompt)

        print(f"Response: {response}")
        print(f"Inference Time: {time_taken:.4f} seconds\n")

# Run inference tests
run_tests(models)

