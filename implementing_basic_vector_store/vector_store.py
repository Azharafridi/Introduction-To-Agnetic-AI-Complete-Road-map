from typing import List, Tuple, Optional
def create_mock_embedding(text: str) -> List[float]:
    length = len(text)
    char_sum = sum(ord(c) for c in text)

    e1 = length / 1000
    e2 = (char_sum % 1000) / 1000
    e3 = ((length * char_sum) % 500) / 500

    return [round(e1, 4), round(e2, 4), round(e3, 4)]

class SimpleVectorStore:
    def __init__(self) -> None:
        self._store: List[Tuple[str, List[float], str]] = []

    def add_document(self, document_id: str, text: str, embedding: List[float]) -> None:
        self._store.append((document_id, embedding, text))

    def get_all_embeddings(self) -> List[List[float]]:
        return [embedding for _, embedding, _ in self._store]

    def get_document_by_id(self, document_id: str) -> Optional[str]:
        for stored_id, _, text in self._store:
            if stored_id == document_id:
                return text
        return None


def main():
    texts = {
        "doc1": "Cats are small domesticated mammals.",
        "doc2": "The Battle of Waterloo took place in 1815.",
        "doc3": "The Pacific Ocean is the largest ocean on Earth.",
        "doc4": "Elephants are the largest land animals.",
        "doc5": "The Great Wall of China is visible from low Earth orbit.",
    }

    vector_store = SimpleVectorStore()

    for doc_id, text in texts.items():
        embedding = create_mock_embedding(text)
        vector_store.add_document(doc_id, text, embedding)

    print("All embeddings:")
    for emb in vector_store.get_all_embeddings():
        print(emb)

    print("\n look for  doc3:")
    print(vector_store.get_document_by_id("doc3"))


if __name__ == "__main__":
    main()