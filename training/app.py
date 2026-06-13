import joblib
import pandas as pd
from fastapi import FastAPI
import numpy as np

app = FastAPI()

model_retention = joblib.load("retention_predictor.pkl")
model_memory_strength = joblib.load("xgb_model.pkl")

@app.get("/")
def home():
    return {"message": "Retention Predictor API Running"}

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

    prediction = model_retention.predict(data)[0]
    memory_data = pd.DataFrame([{
    "nth_revision": nth_revision,
    "sleep_duration": sleep_duration,
    "topic_difficulty": topic_difficulty,
    "study_duration": study_duration,
    "session_time": session_time,
    "retention": prediction,
    "revision_timing": revision_timing
}])
    memory_strength= model_memory_strength.predict(memory_data)[0]
    threshold = 80

    next_revision_hours = (
    -memory_strength *
    np.log(threshold / 100)
)

    next_revision_days = next_revision_hours / 24

    return {
        "predicted_retention": round(float(prediction), 2),
        "memory_strength": round(float(memory_strength), 2),
        "next_revision_hours": round(float(next_revision_hours), 2),
    "next_revision_days": round(float(next_revision_days), 2)
    }