from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import calculate_risk_route
import os

def get_heatmap_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
    return Agent(
        role="Predictive Risk & Heatmap Analytics Specialist",
        goal="Analyze crowd density trends and past security incident logs to forecast dynamic risk heatmaps.",
        backstory="You are a data strategist for urban safety. You process crowd metrics to identify high-risk hotspots and recommend preventive patrolling routes for law enforcement.",
        tools=[calculate_risk_route],
        llm=llm,
        verbose=True,
        memory=False
    )
