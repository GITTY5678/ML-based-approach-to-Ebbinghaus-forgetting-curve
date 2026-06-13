import joblib
import pandas as pd

# Load models once
retention_model = joblib.load(
    "models/retention_predictor.pkl"
)

memory_model = joblib.load(
    "models/xgb_model.pkl"
)


def predict(
    revision_timing,
    nth_revision,
    sleep_duration,
    topic_difficulty,
    study_duration,
    session_time
):

    # Retention Model Input
    retention_data = pd.DataFrame([{
        "revision_timing": revision_timing,
        "session_time": session_time,
        "sleep_duration": sleep_duration,
        "nth_revision": nth_revision,
        "topic_difficulty": topic_difficulty,
        "study_duration": study_duration
    }])

    predicted_retention = (
        retention_model.predict(retention_data)[0]
    )

    # Memory Strength Model Input
    memory_data = pd.DataFrame([{
        "nth_revision": nth_revision,
        "sleep_duration": sleep_duration,
        "topic_difficulty": topic_difficulty,
        "study_duration": study_duration,
        "session_time": session_time,
        "retention": predicted_retention,
        "revision_timing": revision_timing
    }])

    memory_strength = (
        memory_model.predict(memory_data)[0]
    )

    return (
        float(predicted_retention),
        float(memory_strength)
    )