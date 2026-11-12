def extract_text(documents):

    extracted_text = []

    for doc in documents:

        text = doc.page_content

        if not text or not text.strip():
            continue

        extracted_text.append({
            "text": text,
            "metadata": doc.metadata
        })

    return extracted_text