from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # MUST be first

from app.api import router  # import AFTER loading .env

app = FastAPI(
    title="RAG API with LangChain",
    version="1.0"
)

app.include_router(router)  # make sure router is included

@app.get("/")
def health_check():
    return {"status": "RAG API running"}
