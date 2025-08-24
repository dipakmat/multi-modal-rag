"""
Pipeline Module
---------------
Defines the multimodal RAG pipeline.
"""

from modules.loader import load_text, load_pdf, load_image
from modules.embedder import Embedder
from modules.vector_store import VectorStore

class RAGPipeline:
    def __init__(self, embed_model: str, vs_host: str, vs_port: int, collection: str):
        self.embedder = Embedder(embed_model)
        self.vector_store = VectorStore(vs_host, vs_port, collection)

    def ingest_document(self, file_path: str, file_type: str):
        """Ingest multimodal document into vector store."""
        if file_type == "text":
            content = load_text(file_path)
            embedding = self.embedder.embed_text(content)
        elif file_type == "pdf":
            content = load_pdf(file_path)
            embedding = self.embedder.embed_text(content)
        elif file_type == "image":
            content = load_image(file_path)
            embedding = self.embedder.embed_text(content)
        else:
            raise ValueError("Unsupported file type")

        self.vector_store.upsert([embedding], [{"content": content}])

    def query(self, query: str, top_k: int = 5):
        """Query vector DB with user question."""
        query_emb = self.embedder.embed_text(query)
        return self.vector_store.search(query_emb, top_k)
