from config import load_google_llm
# import output parsers from langchain
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
jparser = JsonOutputParser()
llm = load_google_llm()

prompt_template = PromptTemplate.from_template("""
You are a professional football analyst. For the player, {player}, provide info in the following JSON format:
{{
"name": string,
"age": int,
"position": string,
"club": string,
"nationality": string,
"goals": int,
"assists": int,
"trophies": int,
"image_url": string
}}

Image_url should be fetched from real sites like pinterest or google.
"""
)

player_name = input("Enter a football player's name: ")
prompt = prompt_template.format(player=player_name)

response = llm.invoke(prompt)
# structured_output = parser.parse(response)
structured_output = jparser.parse(response)

print(f"Response: {response}")
print(f"Structured Prompt: {structured_output}")