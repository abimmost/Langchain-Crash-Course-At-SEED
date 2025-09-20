from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.prompts import ChatPromptTemplate
from config import load_google_chat_model

chat_model = load_google_chat_model()
loader = PyPDFLoader('./data/ai.pdf')
text_loader = TextLoader('./data/ai.txt')

final_text = text_loader.load()
load_data = loader.load()
    
# print(load_data[0].page_content)
# print("My final text is: ", final_text[0].page_content)
# print("Loaded data: ", load_data)

prompt_template = ChatPromptTemplate.from_messages([
    ('system', "You are a fine-tuned assistant that interacts with the user based solely on the following context: {context}. "),
    ('user', "Please help me {question} about context.")
])

while True:
    user_question = input("\n\nEnter your question: ")
    prompt = prompt_template.format(
        context=final_text,
        question=user_question
    )

    print("Generating response...")
    for part in chat_model.stream(prompt):
        print(part.content, end="", flush=True)
