from app.embeddings.embedding_service import (
    generate_embedding
)

vector = generate_embedding(
    "How do I reset my AWS password?"
)

print("Vector dimensions:", len(vector))
print(vector[:10])