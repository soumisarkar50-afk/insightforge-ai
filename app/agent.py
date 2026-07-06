from google.adk.agents import SequentialAgent

from app.agents.feedback_agent import feedback_agent
from app.agents.prioritization_agent import prioritization_agent
from app.agents.prd_agent import prd_agent
from app.agents.roadmap_agent import roadmap_agent

root_agent = SequentialAgent(
    name="product_strategy_agent",
    description="AI Product Strategy and Feedback Intelligence System",
    sub_agents=[
        feedback_agent,
        prioritization_agent,
        prd_agent,
        roadmap_agent,
    ],
)

