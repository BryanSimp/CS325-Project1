"""
File: webScraper.py
Author: Bryan Simpson
Course: CS325
Description: This script reads a list of URLs from a file (siteList.txt), scrapes all 
             heading tags (h1 to h6) from each website, and writes any headings that 
             are 36 characters or longer to an output file (webPrompts.txt). The script 
             also handles request errors gracefully and skips any blank lines in the 
             URL list.

Requirements:
- Install the necessary dependencies:
    pip install beautifulsoup4 lxml requests
- Ensure siteList.txt exists and contains one URL per line.
"""

from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import requests  # Import requests to make HTTP requests

class Processor:
    def process(self, input_file, output_file):
        raise NotImplementedError("Subclasses must implement this method.")  # Force subclasses to implement this method

class WebScraper(Processor):  # Inherits from Processor base class
    def __init__(self, urls_file):
        self.urls_file = urls_file  # Store the path to the file containing URLs

    def process(self, input_file=None, output_file="webPrompts.txt"):
        with open(self.urls_file, "r") as file:  # Open the file with the list of URLs
            urls = file.read().splitlines()  # Read all lines and split into a list

        with open(output_file, "w", encoding="utf-8") as output:  # Open the output file for writing
            for url in urls:  # Loop through each URL in the list
                if not url.strip():  # Skip empty or whitespace-only lines
                    continue
                try:
                    response = requests.get(url)  # Make an HTTP GET request to the URL
                    response.raise_for_status()  # Raise error for bad status codes
                    soup = BeautifulSoup(response.content, "lxml")  # Parse HTML content with BeautifulSoup
                    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # Find all heading tags
                    for heading in headings:  # Loop through each heading
                        text = heading.get_text(strip=True)  # Get the heading text and strip whitespace
                        if text and len(text) >= 36:  # Only keep headings with 36 or more characters
                            output.write(text + "\n")  # Write valid heading to output file
                except requests.RequestException as e:  # Handle request-related errors
                    print(f"Failed to fetch {url}: {e}")  # Print error message for failed URL