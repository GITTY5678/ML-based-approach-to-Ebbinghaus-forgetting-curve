import streamlit as st

from database.db import (
    get_latest_session,
    get_total_sessions,
    get_average_retention
)

# --------------------------
# Login Protection
# --------------------------

if not st.session_state.get(
    "logged_in",
    False
):
    st.warning(
        "Please login first."
    )
    st.stop()

# --------------------------
# Page Title
# --------------------------

st.title("📊 Dashboard")

# --------------------------
# Database Data
# --------------------------

latest = get_latest_session()

total_sessions = get_total_sessions()

avg_retention = get_average_retention()

# --------------------------
# Latest Session
# --------------------------

if latest:

    retention, next_hours = latest

else:

    retention = 0
    next_hours = 0

# --------------------------
# Overall Metrics
# --------------------------

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Study Sessions",
        total_sessions
    )

with col2:

    st.metric(
        "Average Retention %",
        f"{avg_retention:.2f}%"
    )

# --------------------------
# Latest Session Metrics
# --------------------------

st.divider()

col3, col4 = st.columns(2)

with col3:

    st.metric(
        "Latest Retention %",
        f"{retention:.2f}%"
    )

with col4:

    st.metric(
        "Next Revision",
        f"{next_hours:.2f} Hours"
    )

# --------------------------
# Learning Status
# --------------------------

st.divider()

st.subheader(
    "📚 Learning Status"
)

if retention >= 90:

    st.success(
        "Excellent retention. Revision can wait."
    )

elif retention >= 80:

    st.info(
        "Good retention. Follow the suggested revision schedule."
    )

elif retention >= 70:

    st.warning(
        "Retention is dropping. Revise soon."
    )

else:

    st.error(
        "High forgetting risk. Immediate revision recommended."
    )

# --------------------------
# Summary
# --------------------------

st.divider()

st.info(
    f"""
Latest Retention: {retention:.2f}%

Suggested Next Revision:
{next_hours:.2f} Hours
"""
)