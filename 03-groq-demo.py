import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "how agentic ai is different than traditional ai?",
        }
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion)