from app.rag.embeddings import get_embeddings
from app.rag.vectorstore import load_vectorstore

embeddings = get_embeddings()
vectorstore = load_vectorstore(embeddings)

docs = vectorstore.docstore._dict

print(f"Total chunks indexed: {len(docs)}\n")

# Print first 3 chunks
for i, doc in list(docs.items())[:3]:
    print("---- CHUNK ----")
    print(doc.page_content)
    print("METADATA:", doc.metadata)
    print()
