import streamlit as st
from database import add_user, get_user_by_username, get_all_users as db_get_all_users

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_username(username)
        if user and user['password'] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = user['role']
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")

def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    role = st.selectbox("Role", ["recruiter", "admin"])
    if st.button("Create Account"):
        existing_user = get_user_by_username(new_username)
        if existing_user:
            st.warning("Username already exists.")
        else:
            add_user(new_username, new_password, role)
            st.success("Account created successfully.")

def check_login(username, password):
    user = get_user_by_username(username)
    if user and user['password'] == password:
        return user['role']
    return None

def get_all_users():
    return db_get_all_users()