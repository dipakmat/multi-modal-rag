"""
FastAPI Service for Multi-modal RAG
-----------------------------------
Provides endpoints for document ingestion and querying.
"""

import os
import yaml
from fastapi import FastAPI, UploadFile, Form
from modules.pipeline import RAGPipeline

# Load config
with open("config/config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

api_key = os.getenv("OPENAI_API_KEY", None)
if not api_key:
    raise ValueError("Please set OPENAI_API_KEY environment variable.")

# Initialize pipeline once
pipeline = RAGPipeline(
    embed_model=cfg["embedding_model"],
    vs_host=cfg["qdrant"]["host"],
    vs_port=cfg["qdrant"]["port"],
    collection="rag_collection",
    llm_model=cfg["text_model"],
    api_key=api_key
)

app = FastAPI(title="Multi-modal RAG API", version="1.0")


@app.post("/ingest")
async def ingest(file: UploadFile, file_type: str = Form(...)):
    """
    Ingest a new document into the vector store.

    Args:
        file (UploadFile): File to ingest.
        file_type (str): Type of file (text, pdf, image).

    Returns:
        dict: Success message.
    """
    file_path = f"data/sample_inputs/{file.filename}"
    with open(file_path, "wb") as f_out:
        f_out.write(await file.read())

    pipeline.ingest_document(file_path, file_type)
    return {"status": "success", "file": file.filename, "type": file_type}


@app.post("/query")
async def query(query: str = Form(...), top_k: int = Form(3)):
    """
    Query the RAG pipeline with user input.

    Args:
        query (str): User question.
        top_k (int): Number of docs to retrieve.

    Returns:
        dict: LLM-generated response.
    """
    answer = pipeline.query(query, top_k=top_k)
    return {"query": query, "answer": answer}
