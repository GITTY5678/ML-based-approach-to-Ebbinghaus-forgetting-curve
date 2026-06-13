import streamlit as st

st.set_page_config(
    page_title="Memory Retention System",
    page_icon="🧠"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:

    st.title(
        f"Welcome {st.session_state['username']} 👋"
    )

    st.success(
        "Login Successful"
    )

else:

    st.title(
        "🧠 Memory Retention System"
    )

    st.warning(
        "Please login first."
    )