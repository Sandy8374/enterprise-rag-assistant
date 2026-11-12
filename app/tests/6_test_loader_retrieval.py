
from app.retrieval.retriever import retrieve_documents


query = "How many earned leave days are available?"

results = retrieve_documents(
    query=query,
    top_k=3
)

print("\nUser Query:", query)

print("\nRetrieved Results:")

for i, result in enumerate(results):

    print(f"\n--- Result {i + 1} ---")

    print("Content:")
    print(result["content"])

    print("\nMetadata:")
    print(result["metadata"])

    print("\nDistance:")
    print(result["score"])
