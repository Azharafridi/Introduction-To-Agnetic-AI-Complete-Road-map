



sentences = [
    "The cat sat on the mat.",
    "The dog barked loudly.",
    "A small feline rested on a rug."
]

# Store tuples of (sentence, embedding)
sentence_embeddings = [(s, create_mock_embedding(s)) for s in sentences]

# Print results
print("Sentence Embeddings:")
for s, emb in sentence_embeddings:
    print(f"Sentence: {s}")
    print(f"Embedding: {emb}\n")


# ---------------------------------------
# Question 1.3 (deterministic behavior)
# NOTE: Our original function is already deterministic:
# same input -> same length & same char_sum -> same embedding.
# Still, let's explicitly demonstrate it.
# ---------------------------------------

# Test deterministic output
text = "The cat sat on the mat."
embedding1 = create_mock_embedding(text)
embedding2 = create_mock_embedding(text)

print("Determinism Test:")
print("Embedding 1:", embedding1)
print("Embedding 2:", embedding2)
print("Are they identical?", embedding1 == embedding2)
