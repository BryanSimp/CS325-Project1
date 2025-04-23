# CS325-Project1

This project uses Ollama and Python to open a text file read the contents and respond saying if its Positive, Negative or Neutral.

# How to use

First you will need to have python installed and install the package ollama using pip

```shell
pip install ollama
```

Then you will need to install Ollama onto your machine
Follow along here: [Ollama Install](https://github.com/ollama)

After you have it installed you will need to download some models
Depending on your machine you will want to use one with half your VRAM

To Install a model you will use this command
```shell
ollama run llama3.1
```

Now you should be able to run the python script and recieve 6 output files
Two responses for the three prompts

# CS325-Project 2

This project uses the BeautifulSoup, Requests, and lxml python packages to scrape website pages 
online to gather buisness news heading that will be used with project 1 to determine if they 
are positive, negative or neutral.

# How to use

First you will need to have python installed and install the packages BeautifulSoup, Requests, and lxml using pip

```shell
pip install BeautifulSoup
pip install requests
pip install lxml
```

After these are installed you should be able to run the python file if you have the siteList.txt file
and it contains a list of websites you would like to scrape data from

Once you run the python script it will create a file called webPrompts.txt that contains the headings
you will use with project1.py eventually

# CS325-Project 3

This project combines Project 1 and Project 2 into a unified workflow. The web scraper generates a list of headings, and these 
headings are then analyzed by the local language model (LLM) to determine if they are positive, negative or neutral.

# How to use

First you need to install the dependencies added into this project

```shell
pip install pytest
```

Make sure you have the sites you want to use stored on each line in the siteList.txt

Then all you need to do is run the main.py script and you will recieve an output called
responseP3.txt

The code has been refactored to follow object-oriented principles. The scraping and sentiment analysis functionality
 has been modularized into separate classes (WebScraper, LLMProcessor, and Processor), and inheritance is used to ensure reusability of components.

Requirements: Ensure that Ollama is installed and running on your machine for sentiment analysis to work properly.

# Testing

To use the test.main.py which tests if the siteList.txt has websites in them that can be used that produce output
and the llmGen.py produces an output for every heading in the list and produces the required minimun of 10 outputs
you need to run this command

```shell
pytest test_main.py
```