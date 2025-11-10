# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain
# from langchain.chains import SequentialChain
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def generate_name_and_slogan(product: str) -> dict:
#     llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.8)

#     name_template = PromptTemplate(
#         input_variables=["product"],
#         template="Generate a creative name for a company that makes {product}"
#     )
#     slogan_template = PromptTemplate(
#         input_variables=["company_name"],
#         template="Create a catchy slogan for this company: {company_name}"
#     )
#     name_chain = LLMChain(llm=llm, prompt=name_template, output_key="company_name")
#     slogan_chain = LLMChain(llm=llm, prompt=slogan_template, output_key="slogan")
#     pipeline = SequentialChain(
#         chains=[name_chain, slogan_chain],
#         input_variables=["product"],
#         output_variables=["company_name", "slogan"],
#         verbose=False,
#     )

#     return pipeline({"product": product})

# if __name__ == "__main__":
#     result = generate_name_and_slogan("eco-friendly water bottles")
#     print(result["company_name"])
#     print(result["slogan"])

# the above old version code... not working as its deprecated... so changed to below code

"""
Section 2.1 
Task: 
Create a LangChain application that generates creative product names and slogans using sequential chains. Implement a system where: 
The first step generates a company name based on a product description 
The second step creates a slogan based on the generated company name 
Both steps use OpenAI LLMs model (gpt-4o-mini-2024-07-18) 
Requirements: 
Define two prompt templates: 
name_template: Takes {product} as input, outputs company name 
Template: "Generate a creative name for a company that makes {product}" 
slogan_template: Takes {company_name} as input, outputs slogan 
Template: "Create a catchy slogan for this company: {company_name}" 
Create two LLM chains: 
name_chain with output key "company_name" 
slogan_chain with output key "slogan" 
Combine chains using SequentialChain and generate an output. 
Test with: 
"eco-friendly water bottles" 
(Example output: "AquaGreen Solutions" with slogan "Hydrate Sustainably!") 

"""


from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

load_dotenv()

def generate_name_and_slogan(product: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.8)

    name_template = PromptTemplate(
        input_variables=["product"],
        template="Generate a creative name for a company that makes {product}"
    )
    
    slogan_template = PromptTemplate(
        input_variables=["company_name"],
        template="Create a catchy slogan for this company: {company_name}"
    )
    name_chain = name_template | llm | StrOutputParser()
    
    slogan_chain = slogan_template | llm | StrOutputParser()
    
    pipeline = (
        {"product": RunnablePassthrough()}
        | RunnablePassthrough.assign(company_name=lambda x: name_chain.invoke(x))
        | RunnablePassthrough.assign(slogan=lambda x: slogan_chain.invoke({"company_name": x["company_name"]}))
    )
    
    return pipeline.invoke(product)

if __name__ == "__main__":
    result = generate_name_and_slogan("eco-friendly water bottles")
    print(result["company_name"])
    print(result["slogan"])