from langchain_ollama import ChatOllama

from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
   
)

response = llm.invoke("Hi,How are you ? My Name is Sharad ")

print(response.content)


response = llm.invoke("what is 1+1 ")

print(response.content)

response = llm.invoke("what is my Name? ")

print(response.content)