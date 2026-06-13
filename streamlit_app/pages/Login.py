import streamlit as st

from database.db import login_user

st.title("🔐 Login")

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    user = login_user(
        username,
        password
    )

    if user:

        st.session_state["logged_in"] = True

        st.session_state["username"] = username

        st.success(
            "Login Successful!"
        )
        st.rerun()

    else:

        st.error(
            "Invalid Credentials"
        )