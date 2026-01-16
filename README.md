# PDF Document Q&A Microservice (RAG)

## 📌 Project Overview

This project is a high-performance **Retrieval-Augmented Generation (RAG)** microservice built for the Round 1 Technical Assignment. It allows users to upload PDF documents, which are then processed, indexed, and queried using semantic search to provide accurate answers based on the document's content.

### Key Features

* **FastAPI Ingestion**: Scalable API endpoints for file uploads and querying.
* **Vector Search**: Uses **FAISS** (Facebook AI Similarity Search) for sub-millisecond document retrieval.
* **Semantic Embeddings**: Leverages the `all-MiniLM-L6-v2` transformer model for high-quality text vectorization.
* **Local LLM Integration**: Uses **Ollama (Llama 3.2)** to generate natural language responses from retrieved context.

---

## 🏗️ Architecture

The system follows a standard RAG pipeline:

1. **Extraction**: Text is extracted from uploaded PDFs using `pypdf`.
2. **Chunking**: Text is split into overlapping windows to maintain context.
3. **Vectorization**: Chunks are converted into 384-dimensional embeddings.
4. **Retrieval**: User queries are matched against the FAISS index using L2 distance.
5. **Generation**: The top context chunks are sent to a local LLM to produce a final answer.

---

## 📖 Documentation

For detailed information on the tools and libraries used in this implementation, please refer to the following official documentation:

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [FAISS (Facebook AI Similarity Search)](https://faiss.ai/)
* [Sentence Transformers (SBERT)](https://www.sbert.net/)
* [Ollama API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)

---

## 🛠️ Tech Stack

* **Backend**: FastAPI, Uvicorn
* **ML/AI**: Sentence-Transformers, FAISS, Ollama (Llama 3.2)
* **Data Handling**: PyPDF, NumPy
* **Language**: Python 3.10+

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or higher
* [Ollama](https://ollama.com/)
* Run `ollama pull llama3.2` before starting.



### Automatic Setup

Run the provided setup script to create a virtual environment and install all dependencies:

```bash
chmod +x setup.sh
./setup.sh

```

### Manual Installation

If you prefer to set it up manually:

1. **Create Environment**: `python -m venv env`
2. **Activate**: `source env/Scripts/activate` (Windows)
3. **Install**: `pip install -r requirements.txt`
4. **Run Server**: `uvicorn app.main:app --reload`

---

## 🔌 API Documentation

### 1. Health Check

`GET /health`

* **Test**: `curl.exe http://localhost:8000/health`

### 2. Document Upload

`POST /upload`

* **Test**: `curl.exe -F "file=@document.pdf" http://localhost:8000/upload`

### 3. Ask a Question

`POST /query`

* **Test**:

```powershell
curl.exe -X POST "http://localhost:8000/query" -H "Content-Type: application/json" -d '{\"question\": \"What is the main topic of this document?\"}'

```

---

## 👨‍💻 Author

**Designed and Implemented by Pushpanathan**

---

## 📜 License

This project is licensed under the **MIT License**.

