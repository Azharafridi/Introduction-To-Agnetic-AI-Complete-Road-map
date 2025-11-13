"""
LangChain Vector Store Example
This script demonstrates:
1. Loading text from a file
2. Splitting text into chunks with overlap
3. Creating embeddings using OpenAI
4. Storing embeddings in FAISS
5. Querying the vector store for similar chunks
"""
import os
from typing import List, Tuple
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def load_and_process_text(file_path: str) -> List[Document]:
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=30,
        chunk_overlap=10,
        separator="",
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    
    return chunks


def create_vector_store(chunks: List[Document]) -> FAISS:
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)
    
    return vector_store


def query_vector_store(
    vector_store: FAISS, 
    query: str, 
    top_k: int = 3
) -> List[Tuple[Document, float]]:
    results = vector_store.similarity_search_with_score(query, k=top_k)
    
    return results


def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it before running this script."
        )
    file_path = "data.txt"
    
    print("=" * 60)
    print("LangChain Vector Store Demo\n")
    print("\n1. Loading and splitting text...")
    chunks = load_and_process_text(file_path)
    print(f"   Created {len(chunks)} chunks")
    
    print("\n   Sample chunks:")
    for i, chunk in enumerate(chunks[:3], 1):
        print(f"   Chunk {i}: '{chunk.page_content}'")
        print("\n2. Creating embeddings and FAISS vector store...")
    vector_store = create_vector_store(chunks)
    print("Vector store created successfully")
    
    print("\n3. Querying the vector store...")
    query = input("   Enter your query: ")
    print(f"   Query: '{query}'")
    
    results = query_vector_store(vector_store, query, top_k=3)
    
    print(f"\n   Top 3 most similar chunks:")
    for i, (doc, score) in enumerate(results, 1):
        print(f"\n   Result {i}:")
        print(f"   Text: '{doc.page_content}'")
        print(f"   Similarity Score: {score:.4f}")
    
    print("Vector store loaded successfully")
    

if __name__ == "__main__":
    main()