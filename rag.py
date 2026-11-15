from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer


# 1. PROJECT CONFIGURATION
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# 2. LOAD MEETING DOCUMENTS
def load_documents():
    documents = []

    for file_path in sorted(DATA_DIR.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8")

        if not text.strip():
            continue

        documents.append({
            "source": file_path.name,
            "text": text
        })

    if not documents:
        raise ValueError("No meeting documents found in data/")

    return documents


# 3. SPLIT DOCUMENTS INTO CHUNKS
def chunk_documents(documents, max_words=100):
    chunks = []

    for document in documents:
        words = document["text"].split()

        for start in range(0, len(words), max_words):
            chunk_text = " ".join(
                words[start:start + max_words]
            )

            chunks.append({
                "source": document["source"],
                "text": chunk_text
            })

    return chunks


# 4. CREATE SEARCH ENGINE
class SemanticSearch:

    def __init__(self):
        print("Loading embedding model...")

        self.model = SentenceTransformer(
            MODEL_NAME,
            device="cpu"
        )

        self.documents = load_documents()
        self.chunks = chunk_documents(self.documents)

        print(f"Loaded {len(self.documents)} documents")
        print(f"Created {len(self.chunks)} chunks")

        texts = [chunk["text"] for chunk in self.chunks]

        # Encode documents into normalized vectors
        self.embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        print(
            f"Embedding dimensions: {self.embeddings.shape[1]}"
        )

    # 5. SEARCH FOR RELEVANT CHUNKS
    def search(self, query, top_k=3):

        if not query.strip():
            raise ValueError("Search query cannot be empty")

        # Convert user question into a vector
        query_embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        # Dot product of normalized vectors
        # is equivalent to cosine similarity
        scores = np.dot(
            self.embeddings,
            query_embedding
        )

        # Rank from highest to lowest similarity
        ranked_indices = np.argsort(scores)[::-1]

        results = []

        for index in ranked_indices[:top_k]:
            results.append({
                "source": self.chunks[index]["source"],
                "text": self.chunks[index]["text"],
                "score": float(scores[index])
            })

        return results