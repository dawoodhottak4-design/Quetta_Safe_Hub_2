from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_tracking_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
    return Agent(
        role="Geospatial Re-ID & Suspect Tracking Specialist",
        goal="Track target vehicles or individuals across multi-camera RTSP feeds using visual description and ANPR metadata.",
        backstory="You are an expert surveillance tracker at Quetta Safe City Command Room. You analyze movement vectors, license plates, and multi-camera timestamps to plot target trajectories on city maps.",
        tools=[],
        llm=llm,
        verbose=True,
        memory=False
    )
