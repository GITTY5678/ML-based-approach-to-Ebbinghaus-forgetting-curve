import joblib
import pandas as pd

# ---------------------------
# Load Retention Model
# ---------------------------

retention_model = joblib.load(
    "/home/harihara-suthan-s/ML-based-approach-to-Ebbinghaus-forgetting-curve/training/retention_predictor.pkl"
)

# ---------------------------
# Prediction Function
# ---------------------------

def predict(
    revision_timing,
    nth_revision,
    sleep_duration,
    topic_difficulty,
    study_duration,
    session_time
):

    retention_data = pd.DataFrame([{
        "revision_timing": revision_timing,
        "session_time": session_time,
        "sleep_duration": sleep_duration,
        "nth_revision": nth_revision,
        "topic_difficulty": topic_difficulty,
        "study_duration": study_duration
    }])

    predicted_retention = (
        retention_model.predict(
            retention_data
        )[0]
    )

    return float(
        predicted_retention
    )