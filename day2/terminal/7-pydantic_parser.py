from typing import List
from config import load_google_llm
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, ValidationError
from langchain_core.prompts import PromptTemplate

llm = load_google_llm()

# FORCE LLM TO GIVE IN A SPECIFIC FORMAT

class Person(BaseModel):
    name: str = Field(description="Full name here")
    age: int = Field(description="Age in years")
    description: str = Field(description="A brief description about the person")
    album: List[str]

# DONE WITH OUR TYPES

parser = PydanticOutputParser(pydantic_object=Person)

prompt_template = PromptTemplate.from_template(
    """Based on the nickname of your favourite artist: {artist}, give me the real and the age in the following JSON format:
    {{ 
     "name":string,
     "age":int,
     "description":string,
     "album":list[string]
     }}
     """)

# YOUR FAVOURITE ARTIST HERE

fav_artist = "50Cent"

prompt = prompt_template.format(artist=fav_artist)

response = llm.invoke(prompt)
print(f"Response: {response}")
try:
    parsed_result = parser.parse(response)
    print("Parsed Result: ", parsed_result)
    print("Name: ", parsed_result.name)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))