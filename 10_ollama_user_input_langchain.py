from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gpt-oss:120b-cloud",

)

user_input = input("Enter your message: ")
response = llm.invoke(user_input)

print(response.content)