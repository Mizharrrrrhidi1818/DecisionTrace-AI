from rag import SemanticSearch


def main():
    print("\n=== DecisionTrace AI ===")
    print("Semantic Search Engine\n")

    search_engine = SemanticSearch()

    questions = [
        "Why was the website launch delayed?",
        "Who is responsible for payment integration?",
        "What is the new website launch date?"
    ]

    for question in questions:
        print("\n" + "=" * 60)
        print(f"QUESTION: {question}")

        results = search_engine.search(
            query=question,
            top_k=3
        )

        for rank, result in enumerate(results, start=1):
            print(f"\nRESULT {rank}")
            print(f"Source: {result['source']}")
            print(f"Similarity: {result['score']:.4f}")
            print(f"Text: {result['text'][:350]}")

    print("\n=== Search Completed Successfully ===")


if __name__ == "__main__":
    main()