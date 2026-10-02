from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

def run_safe_hub_pipeline(user_query):
    researcher, analyst, advisor = create_agents()
    tasks = create_tasks(researcher, analyst, advisor, user_query)
    
    crew = Crew(
        agents=[researcher, analyst, advisor],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    return result
