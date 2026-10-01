from crewai import Agent
import os

def get_verification_agent():
    return Agent(
        role="Citizen Intelligence & Verification Specialist",
        goal="Filter, deduplicate, and cross-verify crowdsourced public safety reports before sending them to the Safe City Grid.",
        backstory="You analyze incoming public messages, social media posts, and citizen reports to eliminate spam and verify actionable safety threats.",
        tools=[],
        llm="openai/gpt-oss-20b",
        verbose=True,
        memory=False
    )
