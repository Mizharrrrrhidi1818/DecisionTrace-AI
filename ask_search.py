from rag import SemanticSearch


def main():
    engine = SemanticSearch()

    print("\nDecisionTrace AI - Semantic Search")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Your question: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        results = engine.search(question, top_k=3)

        for rank, result in enumerate(results, start=1):
            print(f"\nResult {rank}")
            print(f"Source: {result['source']}")
            print(f"Similarity: {result['score']:.4f}")
            print(f"Content: {result['text']}\n")


if __name__ == "__main__":
    main()