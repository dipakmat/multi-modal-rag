from modules.embedder import Embedder

def test_embed_text():
    embedder = Embedder()
    vec = embedder.embed_text("This is a test sentence.")
    assert len(vec) > 0
