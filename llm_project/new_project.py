from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
import os
os.environ['OPENAI_API_KEY'] = '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'
loader = CSVLoader(file_path= "./3_project_codebasics_q_and_a/codebasics_faqs.csv",source_column="prompt")
data = loader.load()
# print(data)
instructor_embeddings = HuggingFaceInstructEmbeddings()
google_api_key = "AIzaSyBcePX6AibVKek60KkZc-lx3KCk508clmM"
llm = OpenAI(temperature = 0.7)
poem = llm("Write a 4 line poem of my love for samosa")
print(poem)
