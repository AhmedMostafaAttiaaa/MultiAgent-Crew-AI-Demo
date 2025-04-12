from crewai import Crew
from agents import venue_coordinator, logistics_manager, marketing_communications_agent
from tasks import venue_task, logistics_task, marketing_task

event_management_crew = Crew(
    agents=[venue_coordinator, logistics_manager, marketing_communications_agent],
    tasks=[venue_task, logistics_task, marketing_task],
    verbose=True
)

result = event_management_crew.kickoff()
print("Final Result:", result)
