from config import load_google_llm, weatherContext
from langchain_core.prompts import ChatPromptTemplate

# Import brain and weather data tool

llm = load_google_llm()

city = input("Enter the city you want the weather for: ")

my_tool = weatherContext(city)

messages = [
    ("system", "You are a weather master that answers questions based on context {context} I want you to be their assistant on what to wear, what to eat, how to prepare for the day, based on the context given. Be flexible and always answer users queries based only but only answer about whether queries of what they ask. Never go off topic. Your response should be precise and never more than 100 tokens")
]

chat_template = ChatPromptTemplate.from_messages(messages)

while True:
    user_input = input("USER: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the weather master. Goodbye!")
        break
    messages.append(("user", user_input))
    prompt = chat_template.format_messages(context=my_tool)
    response = llm.invoke(prompt)
    messages.append(("ai", response))
    print("AI: ", response)


# print(f"LLM: {llm}")
# print(f"Tool: {my_tool}")

# Use tool and brain to build application