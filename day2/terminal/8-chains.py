from config import load_google_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# one runnable
# Why -> it receives a prompt and send out output

llm = load_google_llm()

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant that helps the user with to answer {question} about a specific {task}"),
    ('user', "Please help me {task}. Take the role of a {role}")
])

user_role = input("Enter the role you want me to take: ")
user_task = input("Enter the task you want help with: ")
user_question = input("Enter the question you want answered: ")

parser = StrOutputParser()

chain = chat_template | llm | parser

output = chain.invoke({
    "role": user_role,
    "question": user_question,
    "task": user_task
})

print("Output: ", output)
