"""
Main Application
----------------
Entry point for running the multimodal RAG pipeline.
"""

import yaml
from modules.pipeline import RAGPipeline

def main():
    # Load config
    with open("config/config.yaml", "r") as f:
        cfg = yaml.safe_load(f)

    pipeline = RAGPipeline(
        embed_model=cfg["embedding_model"],
        vs_host=cfg["qdrant"]["host"],
        vs_port=cfg["qdrant"]["port"],
        collection="rag_collection"
    )

    # Ingest documents
    pipeline.ingest_document("data/sample_inputs/sample.pdf", "pdf")
    pipeline.ingest_document("data/sample_inputs/sample.jpg", "image")

    # Query system
    results = pipeline.query("Summarize the financial impact of delayed claims in healthcare")
    print("Retrieved Results:", results)

if __name__ == "__main__":
    main()
