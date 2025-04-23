from webScraper import WebScraper  # Import the WebScraper class from webScraper.py
from llmGen import LLMProcessor    # Import the LLMProcessor class from llmGen.py

def stock_checker():
    scraper = WebScraper("siteList.txt")               # Create a WebScraper instance with the list of URLs
    scraper.process(output_file="webPrompts.txt")      # Scrape headings and save results to webPrompts.txt

    llm_processor = LLMProcessor()                     # Create an LLMProcessor instance to classify headings
    llm_processor.process("webPrompts.txt", "responseP3.txt")  # Classify scraped headings and save to responseP3.txt

stock_checker()  # Call the main function to run the entire process