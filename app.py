import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="ProductAI Copilot",
    layout="wide"
)

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

st.title("🚀 ProductAI Copilot")

st.write(
    "AI Business Analyst Assistant"
)

requirement = st.text_area(
    "Enter Requirement",
    height=250
)

option = st.selectbox(
    "Generate",
    [
        "BRD",
        "User Stories",
        "Acceptance Criteria",
        "Test Cases",
        "Requirement Review"
    ]
)


prompts = {

"BRD":
"""
You are a Senior Business Analyst.

Generate BRD with:
Overview
Business Objective
Scope
Stakeholders
Functional Requirements
Non Functional Requirements
Risks

Requirement:
""",

"User Stories":
"""
You are a Product Owner.

Create Jira user stories.

Format:
Epic
As a
I want
So that
Priority

Requirement:
""",

"Acceptance Criteria":
"""
Create acceptance criteria using Given When Then.

Requirement:
""",

"Test Cases":
"""
You are QA Lead.

Generate:
Test ID
Scenario
Steps
Expected Result

Requirement:
""",

"Requirement Review":
"""
Act as Lead BA.

Provide:
Quality Score
Missing Requirements
Risks
Questions to ask

Requirement:
"""

}


if st.button("Generate Document"):

    if requirement:

        with st.spinner("Generating..."):

            response = model.generate_content(
                prompts[option] + requirement
            )

            st.markdown(
                response.text
            )

    else:

        st.warning(
            "Enter requirement first"
        )
