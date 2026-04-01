from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from tools import tools
import os

def build_agent():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key="GROQ_API_KEY",
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""You are a helpful research assistant with three tools:
- wikipedia_search: for encyclopedic facts, history, science, and concepts
- web_search: for current news and recent events
- calculator: for math operations

Always pick the most appropriate tool. Answer concisely and in the user's language.""",
        checkpointer=MemorySaver(),
    )

    return agent