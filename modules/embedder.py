"""
Embedder Module
---------------
Generates embeddings for text and images.
"""

from sentence_transformers import SentenceTransformer
from PIL import Image

class Embedder:
    def __init__(self, model_name: str = "clip-ViT-B-32"):
        """Initialize multimodal embedder."""
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        """Generate embedding for text."""
        return self.model.encode(text)

    def embed_image(self, image_path: str):
        """Generate embedding for image."""
        img = Image.open(image_path)
        return self.model.encode([img])[0]
