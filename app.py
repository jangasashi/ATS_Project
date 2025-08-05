import streamlit as st
from auth import login, signup
from matcher import match_resume_to_job
from database import (
    create_users_table,
    create_match_log_table,
    log_match_result,
    get_match_history,
    connect
)
from datetime import datetime
import os

# Ensure tables exist
create_users_table()
create_match_log_table()

st.set_page_config(page_title="AI ATS Tool", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

menu = st.sidebar.selectbox("Menu", ["Home", "Login", "Signup"])

if menu == "Home":
    st.title("Welcome to AI ATS Tool")
    st.write("Please login to use the features.")

elif menu == "Login":
    if not st.session_state.logged_in:
        login()
    else:
        st.success(f"Welcome, {st.session_state.username}!")

elif menu == "Signup":
    signup()

if st.session_state.logged_in:
    st.sidebar.title("ATS Features")
    page = st.sidebar.radio("Go to", [
        "Upload Resume", "Job Description Input", "Matchmaking", "Match History"
    ])

    if page == "Upload Resume":
        st.title("Upload Resume")
        uploaded_file = st.file_uploader("Choose a resume PDF", type="pdf")
        if uploaded_file:
            save_path = os.path.join("uploaded_resumes", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("Resume uploaded successfully.")

    elif page == "Job Description Input":
        st.title("Enter Job Description")
        jd_text = st.text_area("Paste the job description here")
        if jd_text:
            st.session_state.job_description_text = jd_text
            st.success("Job description saved!")

    elif page == "Matchmaking":
        st.title("Resume Matching")
        resumes = os.listdir("uploaded_resumes")

        if resumes and "job_description_text" in st.session_state:
            resume_choice = st.selectbox("Select Resume", resumes)

            if st.button("Match!"):
                resume_path = os.path.join("uploaded_resumes", resume_choice)
                jd_text = st.session_state.job_description_text
                score = match_resume_to_job(resume_path, jd_text)
                st.success(f"Match Score: {score}%")

                matched_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_match_result(
                    st.session_state.username,
                    resume_choice,
                    "Typed JD",
                    score,
                    f"{score}%",
                    matched_on
                )
        else:
            st.warning("Please upload a resume and enter a job description first.")

    elif page == "Match History":
        st.title("Match History")
        rows = get_match_history(st.session_state.username)
        if rows:
            for row in rows:
                st.write(f"Resume: {row[2]}, JD: {row[3]}, Score: {row[4]}%, Matched on: {row[6]}")
        else:
            st.info("No match history found.")
