# RAG API with LangChain

A **Retrieval-Augmented Generation (RAG)** system using **LangChain** and **FastAPI**.  
This project allows you to ask questions over PDF or TXT documents and receive structured answers along with their sources.

---

## Features

- Load PDF and TXT documents from a folder.
- Split documents into chunks for semantic retrieval.
- Generate vector embeddings using HuggingFace `all-MiniLM-L6-v2`.
- Store and retrieve vectors with FAISS.
- Query documents using **Gemini LLM** from Google via LangChain.
- Returns line-by-line structured answers with sources.
- Exposes a FastAPI endpoint for easy integration.

---

## Folder Structure

```
rag-fastapi/
├── app/
│   ├── rag/
│   │   ├── chain.py          # RAG chain setup
│   │   ├── embeddings.py     # Embeddings configuration
│   │   ├── loader.py         # Document loading
│   │   └── vectorstore.py    # FAISS vectorstore creation and loading
│   ├── api.py                # FastAPI router with /ask endpoint
│   └── main.py               # FastAPI entry point
├── data/
│   └── documents/            # Add your PDFs/TXT files here
├── .env                      # Environment variables (not tracked)
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-fastapi.git
cd rag-fastapi
```

### 2. Create a virtual environment

```bash
python -m venv venv
```
Activate it:

- **Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

### 5. Add documents

Place your PDF or TXT files in:

```
data/documents/
```

Example:

```
data/documents/Report.pdf
data/documents/sample.txt
```

---

### 6. Index documents

Run the indexing script (create `index_documents.py` if not already done):

```bash
python index_documents.py
```

You should see:

```
Documents indexed successfully
```

This creates a FAISS vectorstore in `data/faiss/`.

---

### 7. Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI at:

```
http://127.0.0.1:8000/docs
```

You can test your endpoints here.

---

## API Usage

### Health Check

**GET /**

```json
{
  "status": "RAG API running"
}
```

---

### Ask a Question

**POST /ask**

Request:

```json
{
  "question": "What safety protocols are in the report?"
}
```

Response:

```json
{
  "answer": [
    "The report includes the following safety protocols:",
    "**For Safety of Human:**",
    "*   **Electrical Hazards:**",
    "*   Mandatory use of insulated gloves when handling live electrical connections.",
    "*   Display of safety signs near high-voltage areas.",
    "**For Safety of Equipment:**",
    "*   **Proper Maintenance:**",
    "*   Regular inspections to identify faults in solar panels, inverters, and mounting structures."
  ],
  "sources": [
    "Report.pdf"
  ]
}
```

- `answer`: line-by-line structured summary of relevant content.  
- `sources`: list of documents used to generate the answer.

---

## Notes

- **Chunking & retrieval:**  
  Documents are split into 500-character chunks with 100-character overlap for better context retrieval.

- **Vectorstore:**  
  FAISS is used for fast similarity search of embeddings.

- **Embeddings:**  
  Sentence-transformers model `all-MiniLM-L6-v2` provides semantic embeddings.

- **LLM:**  
  Google Gemini (`gemini-2.5-flash`) generates answers based on retrieved chunks.

---

## Security

- Keep `.env` out of version control.  
- Do not commit FAISS indexes with sensitive content if using private documents.  

---

## Future Improvements

- Include **page numbers** in sources.  
- Support more file types (Word, Excel, etc.).  
- Add authentication to the FastAPI endpoints.  
- Enable **multi-document queries** with ranking.  

---

## License

MIT License

---

## Author

A.J.Ahamed Shahmi – [GitHub Profile](https://github.com/shahmi0519)

