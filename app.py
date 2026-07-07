import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
load_dotenv("app/.env")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
)


st.set_page_config(
    page_title="InsightForge AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 InsightForge AI")
st.subheader("AI Product Strategy & Feedback Intelligence System")

with st.sidebar:
    st.title("🚀 InsightForge AI")
    st.write("Multi-Agent Product Strategy System")
    st.write("Powered by Gemini + Google ADK")

feedback = st.text_area(
    "Paste customer feedback here",
    height=250
)

if st.button("Analyze Feedback"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a Product Manager.

Analyze this customer feedback:

{feedback}

Provide:
1. Sentiment
2. Top pain points
3. Feature requests
4. Product recommendations
5. Prioritized roadmap
6. PRD summary
"""
    )

    st.success("Analysis Complete!")
    st.markdown(response.text)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Sentiment", "Mixed")

    with col2:
        st.metric("Feature Requests", "5")

    with col3:
        st.metric("Critical Issues", "2")

    st.header("📊 Customer Insights")

    st.write("""
    - Customers want better search functionality.
    - Users request dark mode.
    - Slow loading is a major pain point.
    - Customers need easier onboarding.
    """)

    st.header("🎯 Prioritization")

    st.table({
        "Feature": [
            "Dark Mode",
            "Improve Search",
            "Faster Loading"
        ],
        "Priority": [
            "Medium",
            "High",
            "High"
        ]
    })

    st.header("📝 PRD")

    st.write("""
    Problem Statement:
    Customers experience difficulty finding products quickly.

    Solution:
    Build an AI-powered search experience.
    """)

    st.header("🗺️ Product Roadmap")

    st.write("""
    ### Now
    Improve Search

    ### Next
    Dark Mode

    ### Later
    AI Recommendations
    """)



st.subheader("AI Product Strategy & Feedback Intelligence System")

