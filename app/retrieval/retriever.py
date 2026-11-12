
from app.retrieval.similarity_search import similarity_search


def retrieve_documents(query: str, top_k: int = 3):

    results = similarity_search(
        query=query,
        top_k=top_k
    )

    retrieved_documents = []

    for doc, score in results:

        retrieved_documents.append({
            "content": doc.page_content,
            "metadata": doc.metadata,
            "score": score
        })

    return retrieved_documents
