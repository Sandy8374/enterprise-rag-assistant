from app.ingestion.loader import load_document
from app.ingestion.extractor import extract_text

docs = load_document("data/raw/HR_Policy.pdf")

content = extract_text(docs)

for item in content:
    print(item["text"])