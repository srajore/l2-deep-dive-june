from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model="gpt-oss:120b-cloud",
)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Tell me the key achievements of {name} in {bullet_points} bullet points.\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

user_name = input("Enter the name of celebrity ...")
bullet_points = input("Enter the number of bullet points ...")

chain = prompt | llm | parser

response = chain.invoke({"name": user_name, "bullet_points": bullet_points})

print(response)