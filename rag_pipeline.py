from rag import SemanticSearch
from llm import generate_answer


class DecisionTraceAI:

    def __init__(self):
        print("Initializing DecisionTrace AI...")

        # Load our semantic search engine
        self.search_engine = SemanticSearch()

        print("DecisionTrace AI is ready!\n")

    def ask(self, question):

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        # STEP 1: Retrieve relevant meeting notes
        retrieved_chunks = self.search_engine.search(
            query=question,
            top_k=5
        )

        # STEP 2: Generate answer with retrieved context
        answer = generate_answer(
            question=question,
            retrieved_chunks=retrieved_chunks
        )

        # STEP 3: Return answer and evidence
        return {
            "question": question,
            "answer": answer,
            "sources": retrieved_chunks
        }