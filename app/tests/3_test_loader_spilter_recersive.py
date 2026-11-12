from app.ingestion.loader import load_document
from app.ingestion.splitter import split_documents

documents = load_document(
    "data/raw/HR_Policy.pdf"
)

chunks = split_documents(documents)

print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print(f"\nChunk {index + 1}")
    print(chunk.page_content)
    print(chunk.metadata)