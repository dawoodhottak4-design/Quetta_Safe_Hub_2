from crewai import Agent
from tools import calculate_risk_route
import os

def get_heatmap_agent():
    return Agent(
        role="Predictive Risk & Heatmap Analytics Specialist",
        goal="Analyze crowd density trends and past security incident logs to forecast dynamic risk heatmaps.",
        backstory="You are a data strategist for urban safety. You process crowd metrics to identify high-risk hotspots and recommend preventive patrolling routes for law enforcement.",
        tools=[calculate_risk_route],
        llm="openai/gpt-oss-20b",
        verbose=True,
        memory=False
    )
