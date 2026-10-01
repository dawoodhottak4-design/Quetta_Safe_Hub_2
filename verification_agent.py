from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_verification_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
    return Agent(
        role="Citizen Intelligence & Verification Specialist",
        goal="Filter, deduplicate, and cross-verify crowdsourced public safety reports before sending them to the Safe City Grid.",
        backstory="You analyze incoming public messages, social media posts, and citizen reports to eliminate spam and verify actionable safety threats.",
        tools=[],
        llm=llm,
        verbose=True,
        memory=False
    )
