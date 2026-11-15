import unittest
from unittest.mock import patch

from rag import load_documents, chunk_documents
from rag_pipeline import DecisionTraceAI


class TestDecisionTraceAI(unittest.TestCase):

    # TEST 1 - Three documents loaded
    def test_document_count(self):
        documents = load_documents()
        self.assertEqual(len(documents), 3)

    # TEST 2 - Documents contain text
    def test_documents_not_empty(self):
        documents = load_documents()

        for document in documents:
            self.assertTrue(document["text"].strip())

    # TEST 3 - Chunk sizes are valid
    def test_chunking(self):
        documents = load_documents()
        chunks = chunk_documents(documents, max_words=100)

        self.assertGreater(len(chunks), 0)

        for chunk in chunks:
            word_count = len(chunk["text"].split())
            self.assertGreater(word_count, 0)
            self.assertLessEqual(word_count, 100)

    # TEST 4 - Empty question rejected
    @patch("rag_pipeline.SemanticSearch")
    def test_empty_question(self, mock_search):
        ai = DecisionTraceAI()

        with self.assertRaises(ValueError):
            ai.ask("   ")

    # TEST 5 - RAG returns correct structure
    @patch("rag_pipeline.generate_answer")
    @patch("rag_pipeline.SemanticSearch")
    def test_rag_response(self, mock_search, mock_llm):
        fake_sources = [
            {
                "source": "meeting_friday.txt",
                "text": "Launch date: November 27, 2026.",
                "score": 0.85
            }
        ]

        mock_search.return_value.search.return_value = fake_sources
        mock_llm.return_value = (
            "The new launch date is November 27, 2026."
        )

        ai = DecisionTraceAI()
        result = ai.ask("What is the new launch date?")

        self.assertIn("November 27", result["answer"])
        self.assertEqual(len(result["sources"]), 1)

        mock_llm.assert_called_once_with(
            question="What is the new launch date?",
            retrieved_chunks=fake_sources
        )

    # TEST 6 - Sources are preserved
    @patch("rag_pipeline.generate_answer")
    @patch("rag_pipeline.SemanticSearch")
    def test_source_reference(self, mock_search, mock_llm):
        fake_sources = [
            {
                "source": "meeting_friday.txt",
                "text": "Sarah approved the postponement.",
                "score": 0.9
            }
        ]

        mock_search.return_value.search.return_value = fake_sources
        mock_llm.return_value = (
            "Sarah approved the postponement."
        )

        ai = DecisionTraceAI()
        result = ai.ask("Who approved the delay?")

        self.assertEqual(
            result["sources"][0]["source"],
            "meeting_friday.txt"
        )


if __name__ == "__main__":
    unittest.main()