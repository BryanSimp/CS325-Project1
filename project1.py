"""
File: project1.py
Author: Bryan Simpson
Course: CS325
Description: This script loads prompts from text files and passes them to two different 
             local language models to classify them as Positive, Negative, or Neutral. 
             The responses from each model are then saved to separate text files.

Requirements:
- Install the necessary dependencies using `requirements.yaml`
- Ensure Ollama is installed and running on your machine
"""

import ollama  # Importing the Ollama client library for local language model inference

# Initialize the Ollama client
client = ollama.Client()

# Define the models to be used
modelA = "llama3.1"  # First language model
modelB = "gemma2"     # Second language model

# Predefined instruction for sentiment analysis
pre = "Respond to the quote with one word: Positive, Negative, or Neutral."

# Process each prompt and save responses from both models
for i in range(1, 4):  # Loop through prompts 1, 2, and 3
    # Read the prompt from the corresponding file
    with open(f'prompt{i}.txt', 'r') as file:
        prompt = file.read()

    # Generate a response using Model A
    responseA = client.generate(model=modelA, prompt=pre + prompt)

    # Save Model A's response to a file
    with open(f'response{i}A.txt', 'w') as file:
        file.write(responseA.response)

    # Generate a response using Model B
    responseB = client.generate(model=modelB, prompt=pre + prompt)

    # Save Model B's response to a file
    with open(f'response{i}B.txt', 'w') as file:
        file.write(responseB.response)