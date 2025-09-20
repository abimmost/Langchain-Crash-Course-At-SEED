from langchain_core.prompts import PromptTemplate

from config import load_google_llm

llm = load_google_llm()

prompt_template = PromptTemplate.from_template(
    # f"Please based on the topic {topic}, explain the concept to the user as if they're 12y.o."
    "Given the book title '{title}' and author '{author}', provide a clear and concise summary of the book."
)

# where should we accept this input

print("WELCOME TO MY BOOK SUMMARY APP 📚")
print("_"*len("WELCOME TO MY BOOK SUMMARY APP 📚"))

# receive from the user
user_title = input("Enter the book title: ")
user_author = input("Enter the author of the book: ")

print("Generating summary...")
prompt = prompt_template.format(
    title=user_title,
    author=user_author
)

# printing the response
# res = llm.invoke(prompt)
# print(f"Response: {res}")
for part in llm.stream(prompt):
    print(part, end="", flush=True)