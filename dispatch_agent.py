from crewai import Agent
from tools import send_emergency_dispatch
import os

def get_dispatch_agent():
    return Agent(
        role="Autonomous Multi-Agency Response Orchestrator",
        goal="Evaluate incident severity ratings and dispatch immediate alerts to Rescue 1122, Police, or FC units.",
        backstory="You are an emergency response manager responsible for zero-delay dispatches. You convert incoming raw incident logs into structured emergency alerts.",
        tools=[send_emergency_dispatch],
        llm="gemini/gemini-2.5-flash",
        verbose=True,
        memory=False
    )
