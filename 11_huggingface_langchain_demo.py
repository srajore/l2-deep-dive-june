from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token="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"
)

chat_model = ChatHuggingFace(llm=model)

response = chat_model.invoke("Tell me the key achievements of Rohit Sharma in 10 bullet points")

print(response.content)