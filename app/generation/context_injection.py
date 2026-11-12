
from app.retrieval.retriever import retrieve_documents
from app.generation.prompt import prompt
from app.generation.llm import llm


def generate_answer(question: str):

    # Step 1: Retrieve relevant documents
    retrieved_docs = retrieve_documents(
        query=question,
        top_k=3
    )

    # Step 2: Prepare context
    context_parts = []

    for doc in retrieved_docs:

        content = doc["content"]
        metadata = doc["metadata"]

        source = metadata.get("source", "Unknown")
        page = metadata.get("page")

        page_number = (
            page + 1 if page is not None else "Unknown"
        )

        context_parts.append(
            f"""
            Source: {source}
            Page: {page_number}

            Content:
            {content}
            """
        )

    # Step 3: Combine retrieved chunks
    context = "\n\n".join(context_parts)

    # Step 4: Inject context into prompt
    messages = prompt.format_messages(
        context=context,
        question=question
    )

    # Step 5: Send prompt to Gemini
    response = llm.invoke(messages)

    # Extract actual text from Gemini response
    if isinstance(response.content, str):

        answer = response.content

    else:

        answer = "\n".join(
            block["text"]
            for block in response.content
            if isinstance(block, dict)
            and block.get("type") == "text"
        )

    return answer.strip()
