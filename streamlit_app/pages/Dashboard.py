import streamlit as st
from database.db import (
    get_latest_session,
    get_total_sessions,
    get_average_retention
)
from database.db import get_latest_session

if not st.session_state.get(
    "logged_in",
    False
):
    st.warning(
        "Please login first."
    )
    st.stop()

st.title("📊 Dashboard")

latest = get_latest_session()
total_sessions = get_total_sessions()

avg_retention = get_average_retention()

if latest:

    retention, memory_strength, next_hours = latest

else:

    retention = 0
    memory_strength = 0
    next_hours = 0

'''col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Retention %",
        f"{retention:.2f}"
    )

with col2:
    st.metric(
        "Memory Strength",
        f"{memory_strength:.2f}"
    )

with col3:
    st.metric(
        "Next Revision (Hours)",
        f"{next_hours:.2f}"
    )'''
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Study Sessions",
        total_sessions
    )

with col2:
    st.metric(
        "Average Retention %",
        f"{avg_retention:.2f}"
    )

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    st.metric(
        "Latest Retention %",
        f"{retention:.2f}"
    )

with col4:
    st.metric(
        "Memory Strength",
        f"{memory_strength:.2f}"
    )

with col5:
    st.metric(
        "Next Revision (Hours)",
        f"{next_hours:.2f}"
    )

st.divider()

st.info(
    "Latest study session summary"
)

learning_score = (
    avg_retention * 0.5
    +
    memory_strength * 0.5
)
st.metric(
    "Learning Score",
    f"{learning_score:.1f}"
)