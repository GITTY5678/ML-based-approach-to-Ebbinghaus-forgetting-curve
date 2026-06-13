import streamlit as st
import time
from datetime import datetime

from utils.predictor import predict
from utils.revision import calculate_revision_time
from database.db import save_session, get_topic_info

# ---------------------------
# Login Protection
# ---------------------------

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# ---------------------------
# Session State
# ---------------------------

if "study_start_time" not in st.session_state:
    st.session_state.study_start_time = None

if "study_duration" not in st.session_state:
    st.session_state.study_duration = 0

# ---------------------------
# Page Title
# ---------------------------

st.title("📚 Study Session")

# ---------------------------
# Topic Name
# ---------------------------

topic_name = st.text_input("Topic Name")

# ---------------------------
# Sleep Duration
# ---------------------------

sleep_duration = st.number_input(
    "Sleep Duration (Hours)",
    min_value=0.0,
    value=7.0
)

# ---------------------------
# Topic Difficulty
# ---------------------------

difficulty_option = st.selectbox(
    "Topic Difficulty",
    [
        "1 - Very Easy",
        "2 - Easy",
        "3 - Basic",
        "4 - Moderate",
        "5 - Average",
        "6 - Challenging",
        "7 - Hard",
        "8 - Very Hard",
        "9 - Expert",
        "10 - Extremely Difficult"
    ]
)

topic_difficulty = int(
    difficulty_option.split("-")[0].strip()
)

# ---------------------------
# Study Timer
# ---------------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Study"):
        st.session_state.study_start_time = time.time()
        st.success("Study session started!")

with col2:
    if st.button("⏹ Stop Study"):

        if st.session_state.study_start_time:

            duration_seconds = (
                time.time()
                - st.session_state.study_start_time
            )

            st.session_state.study_duration = (
                duration_seconds / 60
            )

            st.success(
                f"Study Duration: {st.session_state.study_duration:.2f} minutes"
            )

        else:
            st.warning("Start a study session first.")

# ---------------------------
# Display Study Duration
# ---------------------------

study_duration = st.session_state.study_duration

if study_duration > 0:
    st.info(
        f"Recorded Study Duration: {study_duration:.2f} minutes"
    )

# ---------------------------
# Auto Detect Revision Info
# ---------------------------

if topic_name:

    topic_info = get_topic_info(topic_name)

    if topic_info:

        nth_revision = topic_info[0] + 1

        last_study_time = datetime.fromisoformat(
            topic_info[1]
        )

        revision_timing = (
            datetime.now()
            - last_study_time
        ).total_seconds() / 3600

    else:

        nth_revision = 1
        revision_timing = 0

    st.info(
        f"Detected Revision Number: {nth_revision}"
    )

    st.info(
        f"Hours Since Last Revision: {revision_timing:.2f}"
    )

# ---------------------------
# Prediction
# ---------------------------

if st.button("Predict"):

    if not topic_name:
        st.error("Please enter a topic name.")
        st.stop()

    retention, memory_strength = predict(
        revision_timing,
        nth_revision,
        sleep_duration,
        topic_difficulty,
        study_duration,
        1  # session_time fixed internally
    )

    hours, days = calculate_revision_time(
        memory_strength
    )

    # Save for Dashboard
    st.session_state["retention"] = retention
    st.session_state["memory_strength"] = memory_strength
    st.session_state["next_hours"] = hours
    st.session_state["next_days"] = days

    # Save to Database
    save_session(
        topic_name,
        revision_timing,
        nth_revision,
        sleep_duration,
        topic_difficulty,
        study_duration,
        1,
        retention,
        memory_strength,
        hours
    )

    # Display Results
    st.success(
        f"Retention: {retention:.2f}%"
    )

    st.info(
        f"Memory Strength: {memory_strength:.2f}"
    )

    st.warning(
        f"Next Revision: {hours:.2f} Hours"
    )

    st.warning(
        f"Next Revision: {days:.2f} Days"
    )