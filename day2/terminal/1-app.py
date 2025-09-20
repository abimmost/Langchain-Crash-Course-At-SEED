from config import load_google_llm, load_google_chat_model

llm = load_google_llm()
chat_model = load_google_chat_model()
print(f"My LLM: {llm}")

res = llm.invoke("Provide a zero-bias response; Based on stats, who is the GOAT of football? not more than 20 words.")
print(f"Response: {res}")
# propmt=>"Programming language for LLMs"

# chat_res = chat_model.invoke("I'm trying to pick out an outfit for myself today")
# print(f"Chat Response: {chat_res}")