"""
File: llmGen.py
Author: Bryan Simpson
Course: CS325
Description: This script loads prompts from text files and passes them to a 
             local language models to classify them as Positive, Negative, or Neutral. 
             The responses are then saved to a new text file called responseP3.txt.

Requirements:
- Install the necessary dependencies using `requirements.yaml`
- Ensure Ollama is installed and running on your machine
"""

import ollama #Import ollama library to use llms

class LLMProcessor: #Define class named LLMProecssor
    def __init__(self, model="llama3.1"): # Define the constructor fo the class
        self.client = ollama.Client() # Initiailze Ollama client instance
        self.model = model # Store model name in an instance variable
        self.instruction = "Respond to the quote with one word: Positive, Negative, or Neutral." # Store insruction for the model in an instance variable

    def classify_headings(self, input_file, output_file): # Define method to classify the headings from the input file
        with open(input_file, 'r') as input_file: # Opens the input file to read
            prompts = input_file.read().splitlines() # Reads each line from input file and stores them into a list

        with open(output_file, 'w') as output_file: # Opens the output file to write to
            for prompt in prompts: # Go through each prompt in the list of prompts
                response = self.client.generate(model=self.model, prompt=self.instruction + prompt) # Send the prompt to the llm to get a response
                output_file.write(response.response + "\n") # Write the response to the output file and create new line
