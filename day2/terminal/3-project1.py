from config import load_google_chat_model

chat_model = load_google_chat_model()
# print(f"My Chat Model: {chat_model}")

# terminal header
print("\nPERSONAL TUTOR ASSISTANT")
print("_"*len("PERSONAL TUTOR ASSISTANT"))

# docstring
"""
I am creating a message array which will help AI format our chats
"""

messages = [
    ("system", "You are a helpful assistant you play a role of a personal tutor.")
]

# Chat Loop

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Tutor: Goodbye! Have a great day!")
        break
    messages.append(("user", user_input))
    print("Tutor: ")
    for part in chat_model.stream(messages):
        print(part.content, end="", flush=True)