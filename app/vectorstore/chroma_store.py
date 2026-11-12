
import os

from dotenv import load_dotenv

from langchain_chroma import Chroma

from app.embeddings.embedding_service import embeddings

load_dotenv()

DB_PATH = os.getenv("CHROMA_DB_PATH")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_PATH
    )

    return vector_store

def load_vector_store():

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_PATH
    )

    return vector_store