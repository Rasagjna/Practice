from langchain_community.document_loaders import TextLoader, csv_loader, UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
import pandas as pd
from sentence_transformers import SentenceTransformer
# loader = TextLoader("nvda_news_1.txt")
# data = loader.load()
# print(data[0].page_content)
# print(data[0].metadata)
# loader = csv_loader.CSVLoader("movies.csv",source_column="title")
# data = loader.load()
# len(data)
# print(data[0].metadata)
# loader = UnstructuredURLLoader(urls = [
#     "https://en.wikipedia.org/wiki/LangChain",
#     "https://en.wikipedia.org/wiki/MS_Dhoni"
    
# ])
# data = loader.load()
# print(len(data))
# print(data[0].metadata)
# print(data[0].page_content)
text = """Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan. 
It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Matt Damon, and Michael Caine. 
Set in a dystopian future where humanity is embroiled in a catastrophic blight and famine, the film follows a group of astronauts who travel through a wormhole near Saturn in search of a new home for humankind.

Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007 and was originally set to be directed by Steven Spielberg. 
Kip Thorne, a Caltech theoretical physicist and 2017 Nobel laureate in Physics,[4] was an executive producer, acted as a scientific consultant, and wrote a tie-in book, The Science of Interstellar. 
Cinematographer Hoyte van Hoytema shot it on 35 mm movie film in the Panavision anamorphic format and IMAX 70 mm. Principal photography began in late 2013 and took place in Alberta, Iceland, and Los Angeles. 
Interstellar uses extensive practical and miniature effects, and the company Double Negative created additional digital effects.

Interstellar premiered in Los Angeles on October 26, 2014. In the United States, it was first released on film stock, expanding to venues using digital projectors. The film received generally positive reviews from critics and grossed over $677 million worldwide ($715 million after subsequent re-releases), making it the tenth-highest-grossing film of 2014. 
It has been praised by astronomers for its scientific accuracy and portrayal of theoretical astrophysics.[5][6][7] Interstellar was nominated for five awards at the 87th Academy Awards, winning Best Visual Effects, and received numerous other accolades."""
splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size=200,
    chunk_overlap=0

)
r_splitter = RecursiveCharacterTextSplitter(
    separators = ["\n\n","\n"," "],
    chunk_size=200,
    chunk_overlap=0

)
# chunks = splitter.split_text(text)
# len(chunks)
# for chunk in chunks:
#     print(len(chunk))
#     print(chunk)
chunks = r_splitter.split_text(text)
len(chunks)
for chunk in chunks:
    print(len(chunk))
    print(chunk)

df = pd.read_csv("sample_text.csv")
# df.shape
encoder = SentenceTransformer("all-mpnet-base-v2")
vectors = encoder.encode(df.text)
print(vectors.shape)
print(vectors)
dim = vectors.shape[1]

import faiss
index=faiss.IndexFlatL2(dim) #euclidian distance
index.add(vectors)
search_query = "I want to buy a polo t-shirt"
vec=encoder.encode(search_query)
# print(vec)
import numpy as np
svec = np.array(vec).reshape(1,-1)
svec.shape
distances,I = index.search(svec,k=2)
print(distances)
print(I)
df.loc[I[0]]
# stuff method: all chunks are combined into a single chunk
# stuff method : drawback : what if the combined chunk exceeds the token limit of LLM?
# map reduce : 
