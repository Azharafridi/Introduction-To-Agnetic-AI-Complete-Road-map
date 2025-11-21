"""
Question 1.1: Write a Python function create_mock_embedding(text) that takes a string and returns a simple list of 3 floating-point numbers as its "embedding." 
Make the numbers slightly different for different inputs (e.g., based on len(text) or character sums) to simulate unique embeddings. 
"""

def create_mock_embedding(text: str):
    length = len(text)
    char_sum = sum(ord(c) for c in text)

    e1 = length / 1000
    e2 = (char_sum % 1000) / 1000
    e3 = ((length * char_sum) % 500) / 500
    return [round(e1, 4), round(e2, 4), round(e3, 4)]

embeddings = create_mock_embedding("is test text for")
print(f"embeddings for qeustion number 1: {embeddings}")


"""
Question 1.2: Use your create_mock_embedding function to generate embeddings for three short sentences: "The cat sat on the mat.", 
"The dog barked loudly.", and "
A small feline rested on a rug." Store these sentences along with their mock embeddings in a list of tuples (sentence, embedding). 
"""

sentences = [
    "The cat sat on the mat.",
    "The dog barked loudly.",
    "A small feline rested on a rug."
]

sentence_embeddings = [(s, create_mock_embedding(s)) for s in sentences]

print("Sentence Embeddings:")
for s, emb in sentence_embeddings:
    print(f"Sentence: {s}")
    print(f"Embedding: {emb}\n")
