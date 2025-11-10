# #from langchain.tools import tool
# import os
# from langchain_openai import ChatOpenAI
# from langchain.agents.agent import AgentExecutor 
# from langchain.agents import create_tool_calling_agent
# from langchain.prompts import ChatPromptTemplate
# from dotenv import load_dotenv
# load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# @tool
# def get_weather(city: str) -> str:
#     """Return today's weather summary for a given city (mocked)."""
#     city_lower = city.strip().lower()
#     data = {
#         "karachi": "32°C, humid, light breeze",
#         "lahore": "28°C, sunny",
#         "islamabad": "25°C, partly cloudy",
#     }
#     return data.get(city_lower, "Weather data unavailable for this city.")


# def run_weather_agent():
#     llm = ChatOpenAI(model="gpt-4o-mini")

#     tools = [get_weather]

#     prompt = ChatPromptTemplate.from_messages([
#         ("system",
#         "You are a helpful assistant. Use tools when useful. "
#         "If you need weather, call the get_weather tool."),
#         ("human", "{input}")
#     ])

#     agent = create_tool_calling_agent(llm, tools, prompt)
#     executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
#     query = input("Enter your query for the Weather Agent: ")
#     result = executor.invoke({"input": query})
#     print(result["output"])


# def main():
#     print("enter your choice to run the agent:")
#     print("1. Weather Agent")
#     choice = input("1. Weather Agent\nChoose (1): ")
#     if choice == "1":
#         run_weather_agent()
#     elif choice == "2":
#         pass
#     elif choice == "3":
#         pass

#     print("Running Weather Agent...")

from dotenv import load_dotenv
from langchainhub import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
load_dotenv()

def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    import datetime

    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time",
    ),
]

prompt = hub.pull("hwchase17/react")

llm = ChatOpenAI(
    model="gpt-4o-mini", temperature=0
)
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
)

response = agent_executor.invoke({"input": "What time is it?"})
print("response:", response)
