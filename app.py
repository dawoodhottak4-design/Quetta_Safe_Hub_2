import streamlit as st
import os
from dotenv import load_dotenv
from crewai import Crew, Process, Task
import folium
from streamlit_folium import st_folium

# Import Modular Agents
from agents.tracking_agent import get_tracking_agent
from agents.dispatch_agent import get_dispatch_agent
from agents.heatmap_agent import get_heatmap_agent
from agents.verification_agent import get_verification_agent

load_dotenv()

st.set_page_config(page_title="Quetta Safe Hub 2.0", layout="wide", page_icon="🛡️")

st.title("🛡️ Quetta Safe Hub 2.0: Autonomous Civic Safety Network")
st.caption("Powered by Multi-Agent AI (CrewAI + Groq) | Balochistan Safe Cities Authority Integration")

# Sidebar - Agent System Status
st.sidebar.header("🤖 Agent System Status")
st.sidebar.success("🟢 Re-ID Tracking Agent: Online")
st.sidebar.success("🟢 Multi-Agency Dispatcher: Online")
st.sidebar.success("🟢 Predictive Heatmap Agent: Online")
st.sidebar.success("🟢 Citizen Verification Agent: Online")

# Layout Tabs
tab1, tab2, tab3 = st.tabs(["🎮 Multi-Agent Command Center", "🗺️ Live Quetta Map & Hotspots", "📊 Executive Analytics"])

with tab1:
    st.subheader("Run Multi-Agent Autonomous Workflow")
    incident_input = st.text_area(
        "Enter Incident Report / CCTV Alert Input:",
        value="A white Toyota Corolla (Plate: ABR-512) was spotted speeding away from Cantt Station after a reported disturbance. High crowd density reported near Serena Chowk."
    )
    
    if st.button("🚀 Trigger Autonomous Agents"):
        if not os.getenv("GROQ_API_KEY"):
            st.error("GROQ_API_KEY is missing in your .env file!")
        else:
            with st.spinner("Agents Analyzing & Processing Incident..."):
                # Initialize Agents
                tracker = get_tracking_agent()
                dispatcher = get_dispatch_agent()
                analyst = get_heatmap_agent()
                verifier = get_verification_agent()
                
                # Define Tasks
                task1 = Task(
                    description=f"Verify this public report for credibility and extract key facts: {incident_input}",
                    expected_output="Verified report summary with credibility score (1-10).",
                    agent=verifier
                )
                
                task2 = Task(
                    description="Identify suspect vehicle/person details and plot potential camera tracking points across Quetta routes.",
                    expected_output="Suspect visual profile and camera tracking sequence.",
                    agent=tracker
                )
                
                task3 = Task(
                    description="Evaluate risk level, determine nearest emergency agency (Rescue 1122 or Police), and execute dispatch alert tool.",
                    expected_output="Emergency dispatch summary and confirmation status.",
                    agent=dispatcher
                )

                # Crew Execution
                crew = Crew(
                    agents=[verifier, tracker, dispatcher],
                    tasks=[task1, task2, task3],
                    process=Process.sequential,
                    verbose=True
                )
                
                result = crew.kickoff()
                
                st.success("Workflow Executed Successfully!")
                st.markdown("### 📋 Multi-Agent Execution Output")
                st.write(result.raw)

with tab2:
    st.subheader("Quetta Live Geospatial Grid")
    # Base Map centered at Quetta
    m = folium.Map(location=[30.1798, 66.9750], zoom_start=13, tiles="CartoDB positron")
    
    # Sample Safe City Camera Pins
    folium.Marker([30.1850, 66.9920], popup="Camera 102 - Cantt Checkpoint", icon=folium.Icon(color="blue", icon="camera")).add_to(m)
    folium.Marker([30.1700, 66.9700], popup="ANPR Camera 04 - Serena Chowk", icon=folium.Icon(color="red", icon="eye")).add_to(m)
    
    st_folium(m, width=1100, height=500)

with tab3:
    st.subheader("System Performance & Integration Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Active Cameras Connected", value="1,200+", delta="Hikvision Network")
    col2.metric(label="Avg Emergency Response Time", value="1.8 Mins", delta="-65% Faster")
    col3.metric(label="Monthly Cloud Operational Cost", value="~$460 USD", delta="PKR 130k-215k")
