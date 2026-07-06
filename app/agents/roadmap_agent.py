from google.adk.agents.llm_agent import Agent

roadmap_agent = Agent(
    model="gemini-2.5-flash",
    name="roadmap_agent",
    description="Creates product roadmaps.",
    instruction="""
Create:

1. Now / Next / Later roadmap
2. Quarterly initiatives
3. Executive summary
4. Stakeholder recommendations

Return the answer in markdown.
"""
)