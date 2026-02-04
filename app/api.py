from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.chain import get_rag_chain
from app.rag.embeddings import get_embeddings
from app.rag.vectorstore import load_vectorstore

router = APIRouter()

# Initialize embeddings, vectorstore, and RAG chain
embeddings = get_embeddings()
vectorstore = load_vectorstore(embeddings)
rag_chain = get_rag_chain(vectorstore)

class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(request: QueryRequest):
    question = request.question

    # Get RAG response
    result = rag_chain(question)

    # Format answer line by line
    answer_lines = result["result"].split("\n")
    formatted_answer = [line.strip() for line in answer_lines if line.strip()]

    # Return structured JSON
    return {
        "answer": formatted_answer,
        "sources": [
            doc.metadata.get("source", "") for doc in result["source_documents"]
        ]
    }
