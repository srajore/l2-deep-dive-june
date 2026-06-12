from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm_client = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

response = llm_client.invoke("could you  tell how can I learn technology(agentic ai) quickly in 3 bullet points?")

print(response)