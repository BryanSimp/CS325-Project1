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