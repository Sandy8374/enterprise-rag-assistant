
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model=os.getenv("EMBEDDING_MODEL")
)


def generate_embedding(text: str):

    vector = embeddings.embed_query(text)

    return vector


def generate_document_embeddings(texts: list[str]):

    vectors = embeddings.embed_documents(texts)

    return vectors
