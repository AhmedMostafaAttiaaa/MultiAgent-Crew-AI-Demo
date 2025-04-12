from crewai import Crew
from agents import venue_coordinator, logistics_manager, marketing_communications_agent
from tasks import venue_task, logistics_task, marketing_task

event_management_crew = Crew(
    agents=[venue_coordinator, logistics_manager, marketing_communications_agent],
    tasks=[venue_task, logistics_task, marketing_task],
    verbose=True
)

""" event_details = {
    'event_topic': "Tech Innovation Conference",
    'event_description': "A gathering of tech innovators "
                         "and industry leaders "
                         "to explore future technologies.",
    'event_city': "San Francisco",
    'tentative_date': "2024-09-15",
    'expected_participants': 500,
    'budget': 20000,
    'venue_type': "Conference Hall"
} """

result = event_management_crew.kickoff(inputs=event_details)
print("Final Result:", result)


""" 
import json
from pprint import pprint

with open('venue_details.json') as f:
   data = json.load(f)

pprint(data)


-------------------- 
from IPython.display import Markdown
Markdown("marketing_report.md")

""""
