from crewai import Agent
import os
from utils import get_openai_api_key, get_anthropic_api_key, get_mistral_api_key

os.environ["OPENAI_API_KEY"] = get_openai_api_key()
os.environ["ANTHROPIC_API_KEY"] = get_anthropic_api_key()
os.environ["MISTRAL_API_KEY"] = get_mistral_api_key()

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_mistralai.chat_models import ChatMistralAI

from tools import simple_tool

llm_openai = ChatOpenAI(model="gpt-3.5-turbo")
llm_anthropic = ChatAnthropic(model="claude-3-haiku-20240307")
llm_mistral = ChatMistralAI(model="open-mistral-7b")

venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Find and book a suitable venue for an event",
    backstory="Expert in event venues and booking logistics.",
    tools=[simple_tool],
    verbose=True,
    llm=llm_openai
)

logistics_manager = Agent(
    role="Logistics Manager",
    goal="Handle event logistics including catering and setup",
    backstory="Ensures smooth execution of logistics.",
    tools=[simple_tool],
    verbose=True,
    llm=llm_anthropic
)

marketing_communications_agent = Agent(
    role="Marketing Agent",
    goal="Promote the event and handle participant communication",
    backstory="Creative marketer for event outreach.",
    tools=[simple_tool],
    verbose=True,
    llm=llm_mistral
)
