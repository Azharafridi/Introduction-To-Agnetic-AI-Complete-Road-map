from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
def sentiment_classifier():
    examples = [
        {"text": "I got a promotion today!", "label": "Happy"},
        {"text": "My dog passed away", "label": "Sad"}
    ]
    example_template = PromptTemplate(
        input_variables=["text", "label"],
        template="Text: {text}\nSentiment: {label}"
    )
    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_template,
        prefix="Classify the sentiment of the following text as either 'Happy' or 'Sad'.\n\nExamples:",
        suffix="\nText: {input}\nSentiment:",
        input_variables=["input"]
    )
    
    model = ChatOpenAI(model="gpt-4o-mini-2024-07-18",api_key=api_key)
    query = input("Enter a text to classify its sentiment: ")
    
    prompt_value = few_shot_prompt.format(input=query)
    
    response = model.invoke(prompt_value)
    
    return response.content
print(sentiment_classifier())

