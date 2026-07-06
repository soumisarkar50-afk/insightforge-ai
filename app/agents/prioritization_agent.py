from google.adk.agents import Agent

prioritization_agent = Agent(
    model="gemini-2.5-flash",
    name="prioritization_agent",
    description="Prioritizes product opportunities.",
    instruction="""
You are a Product Prioritization Agent.

Analyze customer issues and provide:

1. RICE scoring
2. Impact vs Effort matrix
3. Urgency ranking
4. Recommended actions

Return the answer in markdown.
"""
)