import streamlit as st
import pandas as pd
from database.db import get_topic_history
from database.db import get_all_sessions
if not st.session_state.get(
    "logged_in",
    False
):
    st.warning(
        "Please login first."
    )
    st.stop()
st.title("📈 Learning Analytics")

df = get_all_sessions()

if df.empty:

    st.warning(
        "No study sessions available."
    )

else:

    st.subheader(
        "Study Session History"
    )

    st.dataframe(df)

    st.subheader(
        "Retention Trend"
    )

    st.line_chart(
        df["retention"]
    )

    st.subheader(
        "Memory Strength Trend"
    )

    st.line_chart(
        df["memory_strength"]
    )

st.divider()

st.subheader("🔍 Topic Analysis")

topic = st.text_input(
    "Enter Topic Name",
    "Arrays"
)

if st.button("Analyze Topic"):

    topic_df = get_topic_history(topic)

    if topic_df.empty:

        st.warning(
            "No records found."
        )

    else:

        st.dataframe(topic_df)

        st.subheader(
            "Memory Strength Growth"
        )

        st.line_chart(
            topic_df.set_index(
                "nth_revision"
            )["memory_strength"]
        )

        st.subheader(
            "Retention Trend"
        )

        st.line_chart(
            topic_df.set_index(
                "nth_revision"
            )["retention"]
        )