from app.generation.context_injection import generate_answer

print("Starting RAG test...", flush=True)

questions = [
    "How many sick leave days are available?",
    "What are the remote working arrangements?",
    "What is the employee resignation procedure?"
]

for question in questions:

    print("\n" + "=" * 60)

    print("QUESTION:", question)

    answer = generate_answer(question)

    print("\nANSWER:", answer)