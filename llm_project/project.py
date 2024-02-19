
import os
import pickle
from langchain_openai import OpenAI
import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
import streamlit as st
from langchain.chains import RetrievalQAWithSourcesChain
os.environ['OPENAI_API_KEY'] = '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'

llm = OpenAI(temperature=0.9,max_tokens=500)
loaders = UnstructuredURLLoader(urls=[
    "https://en.wikipedia.org/wiki/LangChain",
    "https://en.wikipedia.org/wiki/MS_Dhoni"
])
data = loaders.load()
len(data)
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = r_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()
vectorindex_openai = FAISS.from_documents(docs,embeddings)
#storing vector index create in local
file_path = "vector_index.pkl"
with open(file_path, "wb") as f:
    pickle.dump(vectorindex_openai, f)
if os.path.exists(file_path):
    with open(file_path,"rb") as f:
        vectorIndex = pickle.load(f)

chain =  RetrievalQAWithSourcesChain(llm=llm,retriever = vectorIndex.as_retriever())
query = "Howmuch did Dhoni score in the series held in Vishakapatnam?"        
langchain.debug = True
chain({"question": query}, return_only_outputs = True)

