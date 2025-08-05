#match_report_viewer.py
import streamlit as st
from database import get_match_history
import pandas as pd

def display_match_report():
    st.subheader("📊 Match History Report")
    history = get_match_history()

    if not history:
        st.info("No match history available.")
        return

    df = pd.DataFrame(history, columns=["ID", "Username", "Resume", "Job Description", "Score", "Timestamp"])
    st.dataframe(df, use_container_width=True)