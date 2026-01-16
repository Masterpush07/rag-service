from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
from app.engine import process_pdf, find_context

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    """Mandatory health check endpoint."""
    return {"status": "healthy"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """Accepts a PDF and processes it into the VectorDB."""
    temp_path = f"uploads/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    num_chunks = process_pdf(temp_path)
    return {"message": f"Uploaded {file.filename}", "chunks_created": num_chunks}

@app.post("/query")
def query(request: QueryRequest):
    """Finds relevant context from the PDF."""
    context = find_context(request.question)
    return {
        "question": request.question,
        "retrieved_context": context
    }