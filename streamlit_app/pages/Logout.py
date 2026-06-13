import streamlit as st

st.title("🚪 Logout")

if st.button("Logout"):

    st.session_state.clear()

    st.success(
        "Logged Out"
    )

    st.rerun()