from config import load_google_chat_model

chat_model = load_google_chat_model()
# print(f"My Chat Model: {chat_model}")

messages=[
    ("system", "You are a helpful assistant you play a role of a football analyst."),
    ("user", "Which country won the first ever world cup?")
]

# res = chat_model.invoke(messages)

for part in chat_model.stream("Who won the ballon d'or 2002? Shouldn't be more than a 1000 words."):
    print(part.content, end="", flush=True)
# print(f"Response: {res}") # res.content
