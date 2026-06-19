from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
)

for chunk in llm.stream("Tell me the key achievements of Rohit Sharma in 10 bullet points"):
    print(chunk.text, end=" ")


