import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2') 
chunks = []
index = None

def process_pdf(file_path):
    global chunks, index
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks)
    
    #building Faiss db
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype('float32'))
    return len(chunks)

def find_context(query):
    if index is None:
        return "No document uploaded yet."
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec).astype('float32'), k=2)
    matches = [chunks[i] for i in indices[0]]
    return "\n".join(matches)