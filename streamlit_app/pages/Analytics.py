import streamlit as st
import pandas as pd

from database.db import (
    get_topic_history,
    get_all_sessions
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

st.title("📈 Learning Analytics")

# --------------------------
# All Sessions
# --------------------------

df = get_all_sessions()

if df.empty:

    st.warning(
        "No study sessions available."
    )

else:

    st.subheader(
        "Study Session History"
    )

    st.dataframe(
        df,
        width="stretch"
    )

    # ----------------------
    # Retention Trend
    # ----------------------

    st.subheader(
        "Retention Trend"
    )

    st.line_chart(
        df["retention"]
    )

    # ----------------------
    # Next Revision Trend
    # ----------------------

    st.subheader(
        "Next Revision Hours"
    )

    st.line_chart(
        df["next_revision_hours"]
    )

# --------------------------
# Topic Analysis
# --------------------------

st.divider()

st.subheader(
    "🔍 Topic Analysis"
)

topic = st.text_input(
    "Enter Topic Name",
    "Arrays"
)

if st.button(
    "Analyze Topic"
):

    topic_df = get_topic_history(
        topic
    )

    if topic_df.empty:

        st.warning(
            "No records found."
        )

    else:

        st.dataframe(
            topic_df,
            width="stretch"
        )

        # ------------------
        # Retention Growth
        # ------------------

        st.subheader(
            "Retention vs Revision Number"
        )

        st.line_chart(
            topic_df.set_index(
                "nth_revision"
            )["retention"]
        )

        # ------------------
        # Revision Schedule
        # ------------------

        st.subheader(
            "Next Revision Hours"
        )

        st.line_chart(
            topic_df.set_index(
                "nth_revision"
            )["next_revision_hours"]
        )

        # ------------------
        # Difficulty Analysis
        # ------------------

        avg_retention = (
            topic_df["retention"]
            .mean()
        )

        st.metric(
            "Average Retention",
            f"{avg_retention:.2f}%"
        )