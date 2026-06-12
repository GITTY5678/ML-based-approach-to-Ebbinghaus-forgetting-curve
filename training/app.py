import joblib
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

model = joblib.load("retention_predictor.pkl")

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

    prediction = model.predict(data)[0]

    return {
        "predicted_retention": round(float(prediction), 2)
    }