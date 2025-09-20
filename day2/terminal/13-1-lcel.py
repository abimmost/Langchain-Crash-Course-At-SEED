#...................RUNNABLE SEQUENCE...................

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from config import load_google_llm

llm = load_google_llm()
prompt = ChatPromptTemplate.from_message(
    [
        ('system','You are a friendly assistant translator'),
        ('user', 'Translate "{text}" into {language}')
    ]
)

parser = StrOutputParser()
chain = prompt | llm | parser 
output = chain.invoke({'language':'spanish', 'text':'Good morning'})

prompt_input=[{'language':'spanish', 'text':'Good morning'}]


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from config import load_google_llm

# Load 2 LLMs
llm1 = load_google_llm()
llm2 = load_google_llm()

# Step 1: Prompt for translation
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly tanslator assistant"),
    ("user", "Translate into {language}: {text}")
])

# Step 2: Prompt for JSON formatting
prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a JSON formatter"),
    ("user", "Format this text into JSON with keys: 'language' and 'translation'. Text: {text}")
])

# Parsers
to_str = StrOutputParser()
to_json = JsonOutputParser()

# Chain: Translation -> str -> JSON
chain = prompt1 | llm1 | to_str | prompt2 | llm2 | to_json

# Execute
output = chain.invoke({"language": "spanish", "text":"good morning"})
print("Response: ", output)