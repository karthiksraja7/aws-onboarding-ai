import streamlit as st
from rag_engine import analyze_onboarding

st.title("AWS Application Onboarding AI")

st.write("Enter new application requirements")

app_name = st.text_input("Application Name")

environment = st.selectbox(
    "Environment",
    ["dev", "qa", "prod"]
)

region = st.text_input("AWS Region")

port = st.text_input("Application Port")

services = st.text_input(
    "Required Services (Example: ALB, ECS, RDS)"
)

if st.button("Analyze Onboarding"):

    app_details = f"""
Application Name: {app_name}
Environment: {environment}
Region: {region}
Port: {port}
Services Required: {services}
"""

    result = analyze_onboarding(app_details)

    st.subheader("Analysis Result")

    st.write(result)
