import streamlit as st
import pandas as pd

from database.db import get_revision_schedule
if not st.session_state.get(
    "logged_in",
    False
):
    st.warning(
        "Please login first."
    )
    st.stop()
st.title("📅 Revision Planner")

rows = get_revision_schedule()

if not rows:

    st.warning(
        "No revision schedules found."
    )

else:

    data = []

    for topic, hours, created_at in rows:

        data.append(
            {
                "Topic": topic,
                "Next Revision (Hours)": round(hours, 2),
                "Created At": created_at
            }
        )

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )