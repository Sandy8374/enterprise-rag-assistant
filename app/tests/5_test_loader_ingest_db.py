from app.ingestion.loader import load_document
from app.ingestion.splitter import split_documents

from app.vectorstore.chroma_store import (
    create_vector_store
)

documents = load_document(
    "data/raw/HR_Policy.pdf"
)

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print("Documents successfully indexed!")