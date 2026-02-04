from app.rag.loader import load_documents
from app.rag.embeddings import get_embeddings
from app.rag.vectorstore import create_vectorstore, save_vectorstore

documents = load_documents("data/documents")
embeddings = get_embeddings()

vectorstore = create_vectorstore(documents, embeddings)
save_vectorstore(vectorstore)

print("Documents indexed successfully")