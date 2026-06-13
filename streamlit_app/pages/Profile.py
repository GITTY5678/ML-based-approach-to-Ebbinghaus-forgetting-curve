import streamlit as st

from database.db import create_user

st.title("📝 Signup")

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Signup"):

    success = create_user(
        username,
        password
    )

    if success:

        st.success(
            "Account Created!"
        )

    else:

        st.error(
            "Username Already Exists"
        )