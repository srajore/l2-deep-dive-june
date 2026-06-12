from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm_client = ChatOpenAI(
    model="gpt-4.1-mini",
)

response = llm_client.invoke("could you  tell how can I learn technology(agentic ai) quickly in 3 bullet points?")

print(response)