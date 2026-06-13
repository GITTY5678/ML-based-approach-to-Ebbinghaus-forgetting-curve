import joblib
import pandas as pd
from fastapi import FastAPI
from utils.revision import calculate_revision_time

app = FastAPI()

# ---------------------------
# Load Model
# ---------------------------

model_retention = joblib.load(
    "retention_predictor.pkl"
)

# ---------------------------
# Home Route
# ---------------------------

@app.get("/")
def home():

    return {
        "message": "Retention Predictor API Running"
    }

# ---------------------------
# Prediction Route
# ---------------------------

@app.post("/predict")
def predict_retention(

    revision_timing: float,
    nth_revision: int,
    sleep_duration: float,
    topic_difficulty: int,
    study_duration: float,
    session_time: int

):

    data = pd.DataFrame([{

        "revision_timing": revision_timing,

        "session_time": session_time,

        "sleep_duration": sleep_duration,

        "nth_revision": nth_revision,

        "topic_difficulty": topic_difficulty,

        "study_duration": study_duration

    }])

    predicted_retention = (
        model_retention.predict(data)[0]
    )

    next_revision_hours, next_revision_days = (
        calculate_revision_time(
            predicted_retention
        )
    )

    return {

        "predicted_retention":
        round(
            float(predicted_retention),
            2
        ),

        "next_revision_hours":
        round(
            float(next_revision_hours),
            2
        ),

        "next_revision_days":
        round(
            float(next_revision_days),
            2
        )

    }