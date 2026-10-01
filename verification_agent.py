from crewai import Agent
from langchain_groq import ChatGroq
import os

def get_verification_agent():
    llm = ChatGroq(model_name="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"))
    
    return Agent(
        role="Citizen Intelligence & Verification Specialist",
        goal="Filter, deduplicate, and cross-verify crowdsourced public safety reports before sending them to the Safe City Grid.",
        backstory="You analyze incoming public messages, social media posts, and citizen reports to eliminate spam and verify actionable safety threats.",
        tools=[],
        llm=llm,
        verbose=True,
        memory=False
    )
