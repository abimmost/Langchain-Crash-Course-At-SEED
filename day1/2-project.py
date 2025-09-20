# connecting our envs from .env

import os
import datetime
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GOOGLE_API_KEY)
print(GROQ_API_KEY)

llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, api_key=GROQ_API_KEY)

# SIMPLE FUNCTION: Daily Journal

# By entering your MOOD of EVENT OF THE DAY, the model gives you a reflection and how you should be able to improve your day\

def daily_journal():
    # header
    print("WELCOME TO MY DAILY JOURNAL APP 🏆")
    print("_"*30)

    # get user input
    mood = input("What is your mood now?\n")
    event = input("What happened today?\n")

    prompt = f"Help me reflect on my day today. I'm feeling {mood} right now and {event} happened today"
    print("Reflection from your assistant")
    print("_"*50)
    for part in llm.stream(prompt):
        print(part, end="", flush=True)

# RUN
daily_journal()