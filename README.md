# Multi-modal RAG Project

This project implements a **modular Retrieval-Augmented Generation (RAG) pipeline** for domain-specific use cases.  
It supports **multi-modal data ingestion** (text, PDFs, images) and integrates with a **vector store (Qdrant)** for retrieval.  

---

## 🚀 Features
- Clean, modular, config-driven design.
- Supports text, PDF, and image ingestion.
- Uses **SentenceTransformers** for embeddings.
- Stores vectors in **Qdrant**.
- Configurable via `config/config.yaml`.
- Unit tested and follows coding standards.

---

## 📂 Project Structure
multimodal_rag_project/

│── config/config.yaml

│── data/sample_inputs/

│── modules/ (loader, embedder, vector_store, retriever, pipeline)

│── tests/

│── notebooks/

│── main.py

│── requirements.txt

│── README.md



---

## 🔧 Setup
```bash
git clone <repo_url>
cd multimodal_rag_project
pip install -r requirements.txt
```
---

## 📌 Workflow

🔧 Build image
```
make build
```

▶ Run pipeline

```commandline
export OPENAI_API_KEY=your_api_key
make run
```

🧪 Run tests
```commandline
export OPENAI_API_KEY=your_api_key
make test

```


🌐 Endpoints

Ingest document
```
curl -X POST "http://127.0.0.1:8000/ingest" \
  -F "file=@data/sample_inputs/sample.pdf" \
  -F "file_type=pdf"
```

Query system
```
curl -X POST "http://127.0.0.1:8000/query" \
  -F "query=Summarize the financial impact of delayed claims in healthcare" \
  -F "top_k=3"
```