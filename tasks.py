from crewai import Task

def create_tasks(researcher, analyst, advisor, user_query):
    
    research_task = Task(
        description=(
            f"Investigate and gather information regarding the following topic/area in Quetta: '{user_query}'. "
            "Focus on recent incidents, infrastructure conditions, public safety alerts, and relevant civic updates."
        ),
        expected_output="A structured summary of collected facts, recent incidents, and safety data relevant to the query.",
        agent=researcher
    )

    analysis_task = Task(
        description=(
            "Review the data gathered by the researcher. Categorize the incidents into Risk Levels (High, Medium, Low) "
            "and identify key hazard zones or recurring patterns in Quetta."
        ),
        expected_output="A risk analysis breakdown detailing severity levels, impacted locations, and primary safety concerns.",
        agent=analyst
    )

    advisory_task = Task(
        description=(
            "Based on the risk analysis, generate a clear, professional Public Safety Briefing for Quetta Safe Hub. "
            "Include: 1) Executive Safety Summary, 2) Key Advisories for Citizens, and 3) Recommended Actions for Local Authorities."
        ),
        expected_output="A well-formatted Markdown safety report ready for display on the public dashboard.",
        agent=advisor
    )

    return [research_task, analysis_task, advisory_task]
