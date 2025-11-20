"""
Basic RAG Workflow: Querying, retrieval, LLM generation. Code a simple python code for this. 

"""

import os
import numpy as np
from openai import OpenAI
from typing import List, Tuple
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

DOCUMENTS = [
    "Retrieval-Augmented Generation (RAG) lets LLMs fetch relevant information "
    "from external sources instead of relying only on training data.",

    "Vector databases store embeddings—numerical representations of text—in a "
    "high-dimensional space allowing similarity search.",

    "Embedding models convert text into vectors so similar meaning texts have "
    "similar embeddings.",

    "A basic RAG pipeline: embed documents → store vectors → embed query → retrieve "
    "top matches → feed them into LLM to generate answer."
]

class SimpleVectorDB:
    def __init__(self):
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Please set it in .env")

        self.client = OpenAI(api_key=api_key)
        self.texts: List[str] = []
        self.embeddings = None

    def get_embeddings(self, texts: List[str]) -> np.ndarray:
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        vectors = [np.array(e.embedding, dtype=float) for e in response.data]
        vectors = np.vstack(vectors)
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        return vectors / norms

    def build_index(self, texts: List[str]):
        self.texts = texts
        self.embeddings = self.get_embeddings(texts)

    def search(self, query: str, k: int = 3):
        if self.embeddings is None:
            raise ValueError("Index not built. Call build_index() first.")

        query_emb = self.get_embeddings([query])[0]
        scores = np.dot(self.embeddings, query_emb)
        top_idx = np.argsort(scores)[::-1][:k]
        return [(self.texts[i], float(scores[i])) for i in top_idx]


def generate_answer(query: str, docs: List[Tuple[str, float]]) -> str:
    context = ""
    for i, (text, score) in enumerate(docs, start=1):
        context += f"[Doc {i} | score={score:.3f}]\n{text}\n\n"

    prompt = f"""
Use ONLY the context below to answer the question.
If answer is not contained in the context, say you don't know.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
""".strip()

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text

def main():
    db = SimpleVectorDB()
    db.build_index(DOCUMENTS)

    query = input("enter you query: ")

    print("\n")
    retrieved = db.search(query, k=3)
    print(generate_answer(query, retrieved))


if __name__ == "__main__":
    main()
