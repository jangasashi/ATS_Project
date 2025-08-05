import streamlit as st
from auth import login, signup
from matcher import match_resume_to_job
from database import log_match_result
import os

st.set_page_config(page_title="AI ATS Tool", layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""

# Sidebar navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Login", "Signup"])

# Main sections
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

# Logged-in user menu
if st.session_state.logged_in:
    st.sidebar.title("ATS Features")

    page = st.sidebar.radio("Go to", [
        "Upload Resume", "Upload Job Description", "Matchmaking", "Match History"
    ])

    if page == "Upload Resume":
        st.title("Upload Resume")
        uploaded_file = st.file_uploader("Choose a resume PDF", type="pdf")
        if uploaded_file:
            save_path = os.path.join("uploaded_resumes", uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("Resume uploaded successfully.")

    elif page == "Upload Job Description":
        st.title("Upload Job Description")
        jd_file = st.file_uploader("Choose a JD PDF or TXT", type=["pdf", "txt"])
        if jd_file:
            save_path = os.path.join("uploaded_jds", jd_file.name)
            with open(save_path, "wb") as f:
                f.write(jd_file.getbuffer())
            st.success("Job Description uploaded successfully.")

    elif page == "Matchmaking":
        st.title("Resume Matching")
        resumes = os.listdir("uploaded_resumes")
        jds = os.listdir("uploaded_jds")

        if resumes and jds:
            resume_choice = st.selectbox("Select Resume", resumes)
            jd_choice = st.selectbox("Select Job Description", jds)

            if st.button("Match!"):
                resume_path = os.path.join("uploaded_resumes", resume_choice)
                jd_path = os.path.join("uploaded_jds", jd_choice)
                score = match_resume_to_job(resume_path, jd_path)
                st.success(f"Match Score: {score}%")
                log_match_result(st.session_state.username, resume_choice, jd_choice, score)
        else:
            st.warning("Please upload at least one resume and one JD first.")

    elif page == "Match History":
        import sqlite3
        st.title("Match History")
        conn = sqlite3.connect("ats_data.db")
        c = conn.cursor()
        c.execute("SELECT * FROM match_logs WHERE username=?", (st.session_state.username,))
        rows = c.fetchall()
        if rows:
            for row in rows:
                st.write(f"Resume: {row[2]}, JD: {row[3]}, Score: {row[4]}%")
        else:
            st.info("No match history found.")
        conn.close()