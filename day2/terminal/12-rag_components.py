from langchain_community.document_loaders import PyPDFLoader, TextLoader
from pprint import pprint
from config import load_embeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma, FAISS

embeddings = load_embeddings()
# STEP 1: Data Loading
loader = PyPDFLoader('./data/cameroon_history.pdf')
# text_loader = TextLoader('./data/ai.txt')

final_load = loader.load()
# print(final_load)
# LOADING THE FIRST DOCUMENT
# print(f"My first document is: {final_load[1]}")

# STEP 2: Chunking/Splitting
text_splitter = CharacterTextSplitter(
    separator="namaewa",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False
)

# # SPLIT TEXT

page_content = [doc.page_content for doc in final_load] # Python comprehension syntax
# To use create_documents instead of split_documents
text1 = text_splitter.create_documents(page_content)

# To get metadata, use split_documents not create_documents
text = text_splitter.split_documents(final_load)

# print(text1[1],"\n\n\n\n\n",text1[2])
# print("\n", len(text1[2].page_content))

# Embeddings and Vector Stores
vector_db = Chroma.from_documents(text, embeddings, persist_directory="./chroma_db") # , collection_name="cameroon_history"
# print("Done storing into vector DB")
prompt = "Who is the first president of Cameroon"
response = vector_db.similarity_search(prompt)
print(f"Response: {response}")