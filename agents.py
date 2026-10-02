import os
import streamlit as st
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def get_llm():
    # Streamlit Secrets se API Key read karna
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY nahi mili! Streamlit secrets check karain.")
        st.stop()
    
    # CrewAI LiteLLM standard Gemini endpoint
    return LLM(
        model="gemini/gemini-2.0-flash",
        api_key=api_key,
        temperature=0.3
    )

def create_agents():
    llm = get_llm()
    
    # Standard Web Search Tool (Optional)
    search_tool = SerperDevTool() if st.secrets.get("SERPER_API_KEY") else None
    tools_list = [search_tool] if search_tool else []

    researcher = Agent(
        role="Quetta Incident & Data Researcher",
        goal="Gather clear, factual, and recent information about safety, infrastructure, and civic issues in Quetta.",
        backstory="A dedicated civic data analyst focusing on collecting reliable news and public safety reports in Quetta.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=tools_list
    )

    analyst = Agent(
        role="Civic Risk Assessment Analyst",
        goal="Categorize risks, assess threat levels, and evaluate the severity of reported incidents.",
        backstory="An expert in urban risk management, capable of identifying danger levels, traffic issues, and public infrastructure hazards.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    advisor = Agent(
        role="Public Safety & Action Advisor",
        goal="Formulate clear citizen safety advisories and actionable recommendations for local governance.",
        backstory="A civic safety advocate skilled at converting risk analysis into actionable guidelines for citizens and municipal authorities.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    return researcher, analyst, advisor
