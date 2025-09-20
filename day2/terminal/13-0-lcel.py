from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from config import load_google_llm

prompt = PromptTemplate(
    input_variables=['product_description'],
    template="Provide a brand name for the tech startup: {product_description}"
)

llm = load_google_llm()

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.invoke(product_description="A software development startup")
print("Result: ", result)