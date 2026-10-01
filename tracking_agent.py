from crewai import Agent
from langchain_groq import ChatGroq
import os

def get_tracking_agent():
    llm = ChatGroq(model_name="groq/llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
    
    return Agent(
        role="Geospatial Re-ID & Suspect Tracking Specialist",
        goal="Track target vehicles or individuals across multi-camera RTSP feeds using visual description and ANPR metadata.",
        backstory="You are an expert surveillance tracker at Quetta Safe City Command Room. You analyze movement vectors, license plates, and multi-camera timestamps to plot target trajectories on city maps.",
        tools=[],
        llm=llm,
        verbose=True,
        memory=False
    )
