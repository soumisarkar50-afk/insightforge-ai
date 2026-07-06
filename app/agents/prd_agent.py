from google.adk.agents.llm_agent import Agent

prd_agent = Agent(
    model="gemini-2.5-flash",
    name="prd_agent",
    description="Creates mini PRDs.",
    instruction="""
You are a Product Requirements Document Generator.

Create:

1. Problem Statement
2. User Stories
3. Acceptance Criteria
4. Success Metrics
5. MVP Scope

Return the answer in markdown.
"""
)