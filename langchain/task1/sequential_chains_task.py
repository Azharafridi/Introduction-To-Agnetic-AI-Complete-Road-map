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
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv

load_dotenv()

def generate_name_and_slogan(product: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.8)
    
    # Define prompts
    name_template = PromptTemplate(
        input_variables=["product"],
        template="Generate a creative name for a company that makes {product}"
    )
    
    slogan_template = PromptTemplate(
        input_variables=["company_name"],
        template="Create a catchy slogan for this company: {company_name}"
    )
    
    # Create chains using LCEL
    name_chain = name_template | llm | StrOutputParser()
    
    slogan_chain = slogan_template | llm | StrOutputParser()
    
    # Create sequential pipeline using runnables
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