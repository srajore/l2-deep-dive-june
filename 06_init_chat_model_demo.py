from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

import os

MODEL_ID = os.getenv("MODEL_ID")


llm_client = init_chat_model(
    #model="gpt-4.1-mini"
    #model="groq:qwen/qwen3-32b"
    #model="google_genai:gemini-2.5-flash"
    model=MODEL_ID
)

response = llm_client.invoke("could you  tell how can I learn technology(agentic ai) quickly in 3 bullet points?")

print(response)
