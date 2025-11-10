from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv() 

def run_job_assistant(job_text: str) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0.3)
    resp_prompt = PromptTemplate(
        input_variables=["job_text"],
        template=(
            "Extract the key responsibilities from the following job description.\n"
            "Return 4 to 7 concise bullet points:\n\n{job_text}"
        ),
    )
    resp_chain = LLMChain(llm=llm, prompt=resp_prompt, output_key="responsibilities")
    skills_prompt = PromptTemplate(
        input_variables=["responsibilities"],
        template=(
            "Given these job responsibilities:\n{responsibilities}\n\n"
            "List the top 3 core skills required, comma-separated, no extra text."
        ),
    )
    skills_chain = LLMChain(llm=llm, prompt=skills_prompt, output_key="skills")

    summary_prompt = PromptTemplate(
        input_variables=["responsibilities", "skills"],
        template=(
            "You are drafting a short application summary for candidate Alex.\n"
            "Use the responsibilities and skills below to create a crisp 3 to 4 sentence summary.\n"
            "Keep it positive, specific, and tailored.\n\n"
            "Responsibilities:\n{responsibilities}\n\n"
            "Top skills:\n{skills}\n"
        ),
    )
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

    pipeline = SequentialChain(
        chains=[resp_chain, skills_chain, summary_chain],
        input_variables=["job_text"],
        output_variables=["responsibilities", "skills", "summary"],
        verbose=False,
    )

    return pipeline({"job_text": job_text})

if __name__ == "__main__":
    jd = """We are hiring a Data Analyst to design dashboards, build SQL queries,
    clean large datasets, collaborate with stakeholders, and present insights to leadership.
    Experience with Python, SQL, BI tools, and A/B testing preferred. Strong communication required."""
    out = run_job_assistant(jd)
    print("\n--- Responsibilities ---\n", out["responsibilities"])
    print("\n--- Skills ---\n", out["skills"])
    print("\n--- Summary for Alex ---\n", out["summary"])
