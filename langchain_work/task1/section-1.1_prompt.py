"""
Section 1.1 
Create a LangChain script that uses ChatPromptTemplate to summarize text with the following requirements: 
Use a system message to define the assistant's role: "You are a professional summarization assistant" 
Use a human message template that takes {text} as input 
Generate a 1-sentence summary that captures the key points 
Use OpenAI's chat model (gpt-4o-mini-2024-07-18) 

"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def ChatPromptTemplate_summerization():
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a professional summarization assistant."),
        ("human", "Generate a 1-sentence summary that captures the key points: {user_input}"),
    ])

    user_input = input("Enter text to summarize: ")
    model = ChatOpenAI(model="gpt-4o-mini")

    prompt_value = template.invoke({"user_input": user_input})
    response = model.invoke(prompt_value)
    return response.content

print(ChatPromptTemplate_summerization())

# todo 
"""
check the alternate method to create ChatPromptTemplate using from_template method
"""
