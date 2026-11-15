from rag_pipeline import DecisionTraceAI


def main():

    ai = DecisionTraceAI()

    print("=" * 50)
    print("DecisionTrace AI - Meeting Intelligence")
    print("Type 'exit' to stop.")
    print("=" * 50)

    while True:

        question = input("\nYour question: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        try:
            result = ai.ask(question)

            print("\nAI ANSWER:")
            print(result["answer"])

            print("\nRETRIEVED SOURCES:")

            for source in result["sources"]:
                print(
                    f"- {source['source']} "
                    f"(similarity: {source['score']:.4f})"
                )

        except (ValueError, RuntimeError) as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()