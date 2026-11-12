from app.ingestion.loader import load_document

documents = load_document(
    "data/raw/HR_Policy.pdf"
)

print("Total pages:", len(documents))

for doc in documents:
    print(doc.metadata)
    print(doc.page_content[:500])