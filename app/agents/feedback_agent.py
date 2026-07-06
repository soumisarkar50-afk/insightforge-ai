
from google.adk.agents.llm_agent import Agent

feedback_agent = Agent(
    model="gemini-2.5-flash",
    name="feedback_agent",
    description="Analyzes customer feedback and extracts insights.",
    instruction="""
You are a Product Feedback Analysis Agent.

Analyze customer feedback and provide:

1. Sentiment summary
2. Top complaints
3. Feature requests
4. Major themes
5. Pain points
6. Desired outcomes

Return the answer in markdown.
"""
)


