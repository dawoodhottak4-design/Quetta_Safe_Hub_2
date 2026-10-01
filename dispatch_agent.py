from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import send_emergency_dispatch
import os

def get_dispatch_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
    return Agent(
        role="Autonomous Multi-Agency Response Orchestrator",
        goal="Evaluate incident severity ratings and dispatch immediate alerts to Rescue 1122, Police, or FC units.",
        backstory="You are an emergency response manager responsible for zero-delay dispatches. You convert incoming raw incident logs into structured emergency alerts.",
        tools=[send_emergency_dispatch],
        llm=llm,
        verbose=True,
        memory=False
    )
