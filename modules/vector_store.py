"""
Vector Store Module
-------------------
Handles storage and retrieval from Qdrant vector database.
"""

from qdrant_client import QdrantClient

class VectorStore:
    def __init__(self, host: str = "localhost", port: int = 6333, collection: str = "rag_collection"):
        self.client = QdrantClient(host=host, port=port)
        self.collection = collection

    def upsert(self, embeddings, payloads):
        """Insert documents with embeddings."""
        self.client.upsert(
            collection_name=self.collection,
            points=embeddings,
            payload=payloads
        )

    def search(self, query_vector, top_k: int = 5):
        """Retrieve top-k documents."""
        return self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            limit=top_k
        )
