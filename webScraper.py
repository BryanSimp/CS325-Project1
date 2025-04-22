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

from bs4 import BeautifulSoup # Import BeautifulSoup library for parsing the HTML
import requests # Import requests library to make HTTP requests

class WebScraper: # Define class WebScrapper
    def __init__(self, urls_file): # Define the constructor for the class
        self.urls_file = urls_file # Store the URL file path as an instance variable

    def scrape_headings(self, output_file): # Define the method for scraping headings and writing to output file
        with open(self.urls_file, "r") as file: # Open the URLs file to read from
            urls = file.read().splitlines() # Read each line and stores them in a list

        with open(output_file, "w", encoding="utf-8") as output: # Opens/Creates the output file to store data
            for url in urls: # Go through each url in the urls list
                if not url.strip(): #check if the line is empty or just white space
                    continue # skips to next line if empty or white space

                try: # start a try block to handle possible request errors
                    response = requests.get(url) # Make HTTP get request for the current url
                    response.raise_for_status() # Raises an error for bad responses

                    soup = BeautifulSoup(response.content, "lxml") # Parses the HTML content of the response with BeautifulSoup using lxml parser
                    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # Finds all heading tags from h1 to h6 in the parsed HTML

                    for heading in headings: # Goes through each found heading tag
                        text = heading.get_text(strip=True) # Get the text content of the headding tag and remove any leading or trailing whitespace
                        if text and len(text) >= 36: # Checks if the text is not empty and has a length of 36 characters or more
                            output.write(text + "\n") # Writes the headig text followed by a new line into the output file

                except requests.RequestException as e: # Catch any execption that occures during the HTTP request
                    print(f"Failed to fetch {url}: {e}") # Prints error messages from a failed URL request 
