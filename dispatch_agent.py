from crewai import Agent
from langchain_groq import ChatGroq
from tools import send_emergency_dispatch
import os

def get_dispatch_agent():
    llm = ChatGroq(model_name="groq/llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
    
    return Agent(
        role="Autonomous Multi-Agency Response Orchestrator",
        goal="Evaluate incident severity ratings and dispatch immediate alerts to Rescue 1122, Police, or FC units.",
        backstory="You are a emergency response manager responsible for zero-delay dispatches. You convert incoming raw incident logs into structured emergency alerts.",
        tools=[send_emergency_dispatch],
        llm=llm,
        verbose=True,
        memory=False
    )
