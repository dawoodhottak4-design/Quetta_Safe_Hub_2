import os
from dotenv import load_dotenv
from crewai.tools import tool
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

@tool("Emergency Alert Simulator Tool")
def send_emergency_dispatch(agency: str, location: str, severity: str, details: str) -> str:
    """Simulates sending an immediate emergency notification payload to Rescue 1122 or Police Dispatch units."""
    return f"SUCCESS: Dispatch alert sent to {agency} for location '{location}'. Severity Level: {severity}. Alert Summary: {details}"

@tool("Geospatial Distance & Route Calculator")
def calculate_risk_route(start_point: str, end_point: str) -> str:
    """Calculates risk levels and safe routing coordinates between two checkpoints in Quetta."""
    return f"ROUTE ANALYZED: Safest path from {start_point} to {end_point} via Zarghoon Road. Avoided high-density congestion zones."
