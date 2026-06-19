from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
)

prompt = PromptTemplate(template="Tell me the key achievements of {name} in {bullet_points} bullet points")

user_name = input("Enter the name of celebrity ...")
bullet_points = input("Enter the number of bullet points ...")
#print(prompt.invoke({"name": user_name, "bullet_points": bullet_points}))



response = llm.invoke(prompt.invoke({"name": user_name, "bullet_points": bullet_points}))

print(response.content)