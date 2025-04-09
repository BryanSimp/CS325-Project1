"""
File: webScraper.py
Author: [Bryan Simpson]
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

from bs4 import BeautifulSoup  # Used to parse and extract data from HTML
import requests  # Used to make HTTP requests to web pages

# Read all URLs from the input file
with open("siteList.txt", "r") as file:
    urls = file.read().splitlines()  # Load all lines into a list and remove newline characters

# Open the output file for writing (overwrites if it already exists)
with open("webPrompts.txt", "w", encoding="utf-8") as output_file:
    for url in urls:
        if not url.strip():  # Skip blank lines in the URL list
            continue

        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if the request failed (e.g., 404 or 500)

            # Parse the HTML content of the page
            html_content = response.content
            soup = BeautifulSoup(html_content, "lxml")

            # Find all heading elements (h1 through h6)
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            # Iterate through each heading and write to file if it meets length requirement
            for heading in headings:
                text = heading.get_text(strip=True)  # Extract text and remove leading/trailing whitespace
                if text and len(text) >= 36:  # Only write headings with 36 or more characters
                    output_file.write(text + "\n")

        except requests.RequestException as e:
            # Print an error message if the URL failed to load
            print(f"Failed to fetch {url}: {e}")
