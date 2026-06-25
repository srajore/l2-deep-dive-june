import gradio as gr
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv


load_dotenv()

llm = init_chat_model(
    "groq:openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages([
("system", "You are a helpful assistant."),
("placeholder", "{chat_history}"),
("human", "{input}")
])


chain = prompt | llm | StrOutputParser()


chat_history = []

def chat(user_message:str,_gradio_history):
    chat_history.append(("human", user_message))

    response = chain.invoke({
        "chat_history": chat_history[:-1],
        "input": user_message
    })

    chat_history.append(("ai", response))

    return response


gr.ChatInterface(
    fn=chat
).launch()









