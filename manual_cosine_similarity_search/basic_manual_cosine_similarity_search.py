"""
Question 1.7: Write a Python function calculate_dot_product(vec1, vec2) that takes two lists of numbers (representing vectors) and returns 
their dot product. 
Question 1.8: Write a Python function calculate_magnitude(vec) that takes a list of numbers and returns its magnitude (Euclidean norm). 
Question 1.9: Using calculate_dot_product and calculate_magnitude, implement calculate_cosine_similarity(vec1, vec2) which returns the cosine 
similarity between two vectors. (Formula: (vec1 . vec2) / (||vec1|| * ||vec2||)). Handle division by zero if a magnitude is zero

"""

import math
from typing import List

def calculate_dot_product(vec1: List[float], vec2: List[float]) -> float:
    return sum(a * b for a, b in zip(vec1, vec2))


def calculate_magnitude(vec: List[float]) -> float:
    return math.sqrt(sum(x * x for x in vec))

def calculate_cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot = calculate_dot_product(vec1, vec2)
    mag1 = calculate_magnitude(vec1)
    mag2 = calculate_magnitude(vec2)

    if mag1 == 0 or mag2 == 0:
        return 0.0   

    return dot / (mag1 * mag2)

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Dot Product:", calculate_dot_product(v1, v2))
print("Magnitude v1:", calculate_magnitude(v1))
print("Magnitude v2:", calculate_magnitude(v2))
print("Cosine Similarity:", calculate_cosine_similarity(v1, v2))
