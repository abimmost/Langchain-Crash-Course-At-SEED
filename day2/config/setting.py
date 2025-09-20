import os
import requests
from dotenv import load_dotenv, find_dotenv
from pprint import pprint
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

def environement_variables():
    load_dotenv(find_dotenv())

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # print("API KEYS LOADING...")
    # print(GOOGLE_API_KEY, OPENAI_API_KEY, GROQ_API_KEY)

def load_google_llm():
    # loading our keys
    environement_variables()
    google_llm = GoogleGenerativeAI(
        # pass our configurations here
        model="gemini-2.5-flash", 
        temperature=0.7
        )
    return google_llm

def load_google_chat_model():
    environement_variables()
    google_chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return google_chat

# CONFIGURE WEATHER ENDPOINT/MAKING REQUEST TO WEATHER API HERE

class WeatherAPILoader:
    def __init__(self, city, api_key):
        # initialize properties
        self.city = city
        self.api_key = api_key

    # Create method that loads the data live

    def load(self):
        # pass info to url; city and api key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metrics"
        # Make request and store in response
        # JSON==Dictionary in Python
        response = requests.get(url).json()
        return response

    # def __init__(self, api_key):
    #     self.api_key = api_key
    #     self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    # def get_weather(self, city):
    #     params = {
    #         'q': city,
    #         'appid': self.api_key,
    #         'units': 'metric'
    #     }
    #     response = requests.get(self.base_url, params=params)
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         return {"error": "City not found or API request failed."}

# Write function to be used anywhere in project
def weatherContext(city):
    # Initialize or create an instance of the class
    environement_variables()
    weatherData = WeatherAPILoader(city=city, api_key=os.getenv("WEATHER_API_KEY"))

    response = weatherData.load()
    return response

def load_embeddings():
    environement_variables()
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Test with sample text
    # Embeddings work by converting text to numerical representations(vectors) that capture meaning

    sample_text = [
        "The weather is beautiful today.",
        "It's a sunny and pleasant day outside.",
        "I love going for walks when the weather is nice.",
        "Machine learning is fascinating."
        ]

    # Generate embeddings for multiple texts at once
    # This is more efficient than generating them one by one
    # embedded_docs = embeddings.embed_documents(sample_text)
    # print("Generating embeddings for sample text...\n","-",*50embedded_docs)
    return embeddings

# load_embeddings()