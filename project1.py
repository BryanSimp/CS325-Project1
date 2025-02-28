import ollama

client = ollama.Client()

modelA = "llama3.1"
modelB = "gemma2"
pre = "Respond to the quote with one word Positive, Negative or Neutral"

#Prompt 1---------------------------------------------------
with open('prompt1.txt','r') as file:
    prompt = file.read()

responseA = client.generate(model=modelA, prompt=pre+prompt)

with open('response1A.txt','w') as file:
    file.write(responseA.response)

responseB = client.generate(model=modelB, prompt=pre+prompt)

with open('response1B.txt','w') as file:
    file.write(responseB.response)

#Prompt 2---------------------------------------------------
with open('prompt2.txt','r') as file:
    prompt = file.read()

responseA = client.generate(model=modelA, prompt=pre+prompt)

with open('response2A.txt','w') as file:
    file.write(responseA.response)

responseB = client.generate(model=modelB, prompt=pre+prompt)

with open('response2B.txt','w') as file:
    file.write(responseB.response)

#Prompt 3---------------------------------------------------
with open('prompt3.txt','r') as file:
    prompt = file.read()

responseA = client.generate(model=modelA, prompt=pre+prompt)

with open('response3A.txt','w') as file:
    file.write(responseA.response)

responseB = client.generate(model=modelB, prompt=pre+prompt)

with open('response3B.txt','w') as file:
    file.write(responseB.response)