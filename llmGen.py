"""
File: llmGen.py
Author: Bryan Simpson
Course: CS325
Description: This script loads prompts from text files and passes them to a 
             local language model to classify them as Positive, Negative, or Neutral. 
             The responses are then saved to a new text file called responseP3.txt.

Requirements:
- Install the necessary dependencies using `requirements.yaml`
- Ensure Ollama is installed and running on your machine
"""

import ollama  # Import the Ollama library to use local language models

class Processor:
    def process(self, input_file, output_file):
        raise NotImplementedError("Subclasses must implement this method.")  # Force subclasses to implement this method

class LLMProcessor(Processor):  # Inherits from the Processor base class
    def __init__(self, model="llama3.1"):
        self.client = ollama.Client()  # Create an Ollama client instance
        self.model = model  # Store the model name
        self.instruction = "Respond to the quote with one word: Positive, Negative, or Neutral."  # Set classification prompt

    def process(self, input_file, output_file):
        with open(input_file, 'r') as f:  # Open the input file for reading
            prompts = f.read().splitlines()  # Read all lines and split them into a list

        with open(output_file, 'w') as f:  # Open the output file for writing
            for prompt in prompts:  # Loop through each prompt
                response = self.client.generate(model=self.model, prompt=self.instruction + prompt)  # Get LLM response
                f.write(response.response + "\n")  # Write response to output file