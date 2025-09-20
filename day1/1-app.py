# connecting our envs from .env

import os
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAI

# STEP 1:
load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GOOGLE_API_KEY)
print(GROQ_API_KEY)

# STEP 2: CONNECTING LLMs

llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, api_key=GROQ_API_KEY)
res = llm.invoke("Say something stupid")
print(f"response from AI: ")

# STREAMING
# With streaming, as the AI generates, the output displays immediately

for part in llm.stream("What is wikenigma"):
    print(part, end="", flush=True)

