"""
Question 1.3: Modify create_mock_embedding to ensure that if the input text is identical, the exact same mock embedding is returned. 
This simulates deterministic embedding models.  

"""

def create_mock_embedding_deterministic(text: str):
    length = len(text)
    char_sum = sum(ord(c) for c in text)

    e1 = length / 1000
    e2 = (char_sum % 1000) / 1000
    e3 = ((length * char_sum) % 500) / 500

    embedding = [round(e1, 4), round(e2, 4), round(e3, 4)]
    return embedding

print(create_mock_embedding_deterministic("Hello"))
print(create_mock_embedding_deterministic("world")) 
