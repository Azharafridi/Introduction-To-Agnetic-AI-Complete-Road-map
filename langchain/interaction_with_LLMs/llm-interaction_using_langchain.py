

## Google gemini LLM Interaction using Langchain
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def google_gemini_llm_interaction() -> str:

    llm = GoogleGenerativeAI(model="gemini-2.5-flash", api_key=GEMINI_API_KEY)
    query = input("Enter your query: ")
    response = llm.invoke(query)
    print(f"Response: {response}")


def chat_model_interaction() -> str:

    chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", api_key=GEMINI_API_KEY)
    input_text = input("Enter your text to explain: ")
    messages = [
        ("system", "You are an AI assistant answer to the question user asking not too long but short if they want: "),
        ("human", "{input_text}"),
    ]
    response = chat_model.invoke(messages)
    print(response.content)



def main():
    print("enter your choice: ")
    print("1. Google Gemini LLM Interaction")
    print("2. Google Gemini Chat Model Interaction")
    choice = int(input("Choice: "))
    if choice == 1:
        google_gemini_llm_interaction() 
    elif choice == 2:
        chat_model_interaction()
    else:
        print("Invalid choice")
main()
