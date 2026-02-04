from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def create_vectorstore(documents, embeddings):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def save_vectorstore(vectorstore, path="data/faiss"):
    vectorstore.save_local(path)


def load_vectorstore(embeddings, path="data/faiss"):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
