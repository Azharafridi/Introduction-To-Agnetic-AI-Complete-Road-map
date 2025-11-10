from langchain.chains.combine import  SequentialChain
from langchain_openai import OpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
# Initialize the OpenAI model with the desired temperature
llm = OpenAI(temperature=0.7)

# Define the template for generating a rap
rap_template = """
You are a Punjabi Jatt rapper, like AP Dhillon or Sidhu Moosewala.

Given two topics, it is your job to create a rhyme of two verses and one chorus
for each topic.

Topic: {topic1} and {topic2}

Rap:
"""

# Create the prompt template for the rap
rap_prompt_template = PromptTemplate(input_variables=["topic1", "topic2"], template=rap_template)

# Create the LLMChain for generating the rap
rap_chain = LLMChain(llm=llm, prompt=rap_prompt_template, output_key="rap")

# Define the template for writing a rap review
review_template = """
You are a rap critic from Rolling Stone magazine and Metacritic.

Given a rap, it is your job to write a review for that rap.

Your review style should be scathing, critical, and no holds barred.

Rap:
{rap}

Review from the Rolling Stone magazine and Metacritic critic of the above rap:
"""

# Create the prompt template for the review
review_prompt_template = PromptTemplate(input_variables=["rap"], template=review_template)

# Create the LLMChain for writing the review
review_chain = LLMChain(llm=llm, prompt=review_prompt_template, output_key="review")

# Combine the chains into a SequentialChain
overall_chain = SequentialChain(
    chains=[rap_chain, review_chain],
    input_variables=["topic1", "topic2"],
    output_variables=["rap", "review"],
    verbose=True
)

# Run the overall chain with the given topics
result = overall_chain({"topic1": "Tractors and sugar canes", "topic2": "Dasuya, Punjab"})