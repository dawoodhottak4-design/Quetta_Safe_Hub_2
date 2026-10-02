from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

def run_safe_hub_pipeline(user_query):
    # Agents initialization
    researcher, analyst, advisor = create_agents()
    
    # Tasks creation
    tasks = create_tasks(researcher, analyst, advisor, user_query)
    
    # Sequential Crew setup (Simple and reliable)
    crew = Crew(
        agents=[researcher, analyst, advisor],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    return result
