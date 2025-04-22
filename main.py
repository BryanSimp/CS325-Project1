from webScraper import WebScraper # Imports the WebScraper class from the webScraper module
from llmGen import LLMProcessor # Imports the LLMProcessor class from the llmGen module

# Step 1: Scrape headings # Comment indicating the start of the web scraping step
scraper = WebScraper("siteList.txt") # Creates an instance of the WebScraper class, passing the input file name
scraper.scrape_headings("webPrompts.txt") # Calls the scrape_headings method to scrape URLs from siteList.txt and save to webPrompts.txt

# Step 2: Run headings through LLM # Comment indicating the start of the LLM processing step
llm_processor = LLMProcessor() # Creates an instance of the LLMProcessor class (using the default model)
llm_processor.classify_headings("webPrompts.txt", "responseP3.txt") # Calls the classify_headings method to read from webPrompts.txt, process with the LLM, and save to responseP3.txt