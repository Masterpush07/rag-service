#!/bin/bash

# 1. Create a virtual environment
echo "Step 1: Creating virtual environment..."
python -m venv env

# 2. Activate the environment
echo "Step 2: Activating environment..."
source env/Scripts/activate || source env/bin/activate

# 3. Install required libraries
echo "Step 3: Installing dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn pypdf sentence-transformers faiss-cpu python-multipart requests

# 4. Create necessary folders
echo "Step 4: Setting up folders..."
mkdir -p uploads data

# 5. Launch the FastAPI server
echo "Step 5: Launching the API server..."
echo "Access the API at: http://127.0.0.1:8000"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload