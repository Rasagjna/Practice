from langchain.document_loaders import TextLoader
loader = TextLoader("nvda_news_q.txt")
data = loader.load()
print(data)
