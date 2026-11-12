
from app.vectorstore.chroma_store import load_vector_store


def similarity_search(query: str, top_k: int = 3):

    # Load existing vector database
    vector_store = load_vector_store()

    # Perform semantic similarity search
    results = vector_store.similarity_search_with_score(
        query=query,
        k=top_k
    )

    return results
