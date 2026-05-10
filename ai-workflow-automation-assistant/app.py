import streamlit as st

st.set_page_config(
    page_title="AI Workflow Automation Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Workflow Automation Assistant")

st.write(
    "A productivity assistant that helps transform business text into summaries, tasks, emails, and action plans."
)

user_input = st.text_area(
    "Paste your business message, meeting notes, or task request here:",
    height=200
)

option = st.selectbox(
    "Choose what you want to generate:",
    [
        "Summary",
        "Task List",
        "Professional Email",
        "Action Plan",
        "Priority Analysis"
    ]
)

def generate_output(text, mode):

    if not text.strip():
        return "Please enter some text first."

    if mode == "Summary":
        return f"""
### Summary

This input discusses important business-related content that requires organization and follow-up.

Main content preview:
{text[:120]}...
"""

    elif mode == "Task List":
        return """
### Task List

- Review the provided information
- Identify key requirements
- Organize priorities
- Prepare action items
- Follow up with stakeholders
"""

    elif mode == "Professional Email":
        return """
### Professional Email Draft

Subject: Follow-up Regarding Project Tasks

Dear Team,

I hope you are doing well.

Please review the provided information and proceed with the required tasks accordingly. Let me know if additional clarification is needed.

Best regards,
Dhay Alsuwat
"""

    elif mode == "Action Plan":
        return """
### Action Plan

1. Understand the request
2. Break tasks into smaller steps
3. Define priorities
4. Assign responsibilities
5. Monitor progress
"""

    elif mode == "Priority Analysis":
        return """
### Priority Analysis

- High Priority → urgent tasks
- Medium Priority → important but not urgent
- Low Priority → future improvements
"""

if st.button("Generate"):
    result = generate_output(user_input, option)
    st.markdown(result)
