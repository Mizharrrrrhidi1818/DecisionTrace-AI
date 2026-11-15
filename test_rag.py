from rag_pipeline import DecisionTraceAI


def main():

    print("\n=== DecisionTrace AI: RAG Test ===\n")

    # Initialize the application
    ai = DecisionTraceAI()

    # Our first question
    question = "Why was the website launch postponed?"

    print(f"QUESTION: {question}\n")

    # Run the complete RAG pipeline
    result = ai.ask(question)

    # Display AI-generated answer
    print("AI ANSWER:")
    print(result["answer"])

    # Display supporting evidence
    print("\nRETRIEVED EVIDENCE:")

    for index, source in enumerate(
        result["sources"], start=1
    ):
        print(f"\n{index}. {source['source']}")
        print(f"Similarity: {source['score']:.4f}")
        print(f"Content: {source['text'][:250]}")

    print("\n=== RAG Test Completed ===")


if __name__ == "__main__":
    main()
    