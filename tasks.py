from crewai import Task
from agents import venue_coordinator, logistics_manager, marketing_communications_agent

venue_task = Task(
    description="Find and book a venue for 100 people on 15th May.",
    expected_output="Venue booking confirmation with details.",
    agent=venue_coordinator
)

logistics_task = Task(
    description="Arrange catering and equipment for 100 participants.",
    expected_output="Confirmation of catering and equipment setup.",
    agent=logistics_manager
)

marketing_task = Task(
    description="Promote the event and email all potential participants.",
    expected_output="Marketing plan and email campaign result.",
    agent=marketing_communications_agent
)
