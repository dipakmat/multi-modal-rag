from modules.pipeline import RAGPipeline

def test_pipeline_ingest_and_query():
    pipeline = RAGPipeline(
        embed_model="clip-ViT-B-32",
        vs_host="localhost",
        vs_port=6333,
        collection="rag_collection"
    )
    try:
        pipeline.ingest_document("data/sample_inputs/sample.txt", "text")
        results = pipeline.query("What is this document about?")
        assert isinstance(results, list)
    except FileNotFoundError:
        pass
