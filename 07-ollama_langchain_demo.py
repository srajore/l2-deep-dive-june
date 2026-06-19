from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
    temperature=0.0,
    top_p=1.0,
    top_k=0,
)

response = llm.invoke("Tell me the key achievements of Rohit Sharma in 10 bullet points")

print(response.content)