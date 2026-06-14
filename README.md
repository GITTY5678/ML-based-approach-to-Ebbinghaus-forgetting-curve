# 🧠 ML-Based Approach to the Ebbinghaus Forgetting Curve

An intelligent learning assistant that predicts memory retention and recommends personalized revision schedules using Machine Learning and the Ebbinghaus Forgetting Curve.

---

# 📌 Overview

Traditional study methods use fixed revision schedules for everyone.

This project introduces a personalized revision recommendation system that considers:

* Revision history
* Study duration
* Sleep duration
* Topic difficulty
* Time since previous revision

The system predicts a learner's retention percentage and recommends the optimal time for the next revision.

---

# 🚀 Features

## User Authentication

* Signup
* Login
* Session Management

---

## Smart Study Tracking

* Topic-based study sessions
* Built-in study timer
* Automatic study duration tracking

---

## Automatic Revision Detection

The system automatically determines:

* Current revision number
* Hours since last revision

No manual calculation required.

---

## Retention Prediction

Machine Learning model predicts:

```text
Retention Percentage (%)
```

based on study behavior and revision history.

---

## Revision Recommendation

The system recommends:

```text
Next Revision Time
```

in:

* Hours
* Days

based on predicted retention.

---

## Learning Analytics

Visual dashboards for:

* Retention trends
* Topic-wise analysis
* Study session history
* Revision recommendations

---

# 🏗 Project Architecture

```text
User Studies
      ↓
Study Timer
      ↓
Automatic Revision Detection
      ↓
Retention Prediction Model
      ↓
Revision Recommendation Function
      ↓
Database Storage
      ↓
Analytics Dashboard
```

---

# 🧮 Machine Learning Features

The retention model uses:

| Feature          | Description               |
| ---------------- | ------------------------- |
| revision_timing  | Hours since last revision |
| nth_revision     | Current revision count    |
| sleep_duration   | Hours slept               |
| topic_difficulty | Difficulty level (1-10)   |
| study_duration   | Study time in minutes     |
| session_time     | Session identifier        |

---

# 📊 Output

The model predicts:

```text
Retention Percentage
```

Example:

```json
{
  "predicted_retention": 92.45,
  "next_revision_hours": 48.0,
  "next_revision_days": 2.0
}
```

---

# 🗂 Project Structure

```text
streamlit_app/

├── app.py

├── pages/
│   ├── Dashboard.py
│   ├── Study_Session.py
│   ├── Analytics.py
│   └── Profile.py

├── database/
│   ├── db.py
│   └── schema.sql

├── models/
│   └── retention_predictor.pkl

├── assets/
│   ├── logo.png
│   └── styles.css

├── utils/
│   ├── predictor.py
│   └── revision.py

└── memory_retention.db
```

---

# 💾 Database Schema

## Users

```sql
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
);
```

## Study Sessions

```sql
CREATE TABLE study_sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_name TEXT,
    revision_timing REAL,
    nth_revision INTEGER,
    sleep_duration REAL,
    topic_difficulty INTEGER,
    study_duration REAL,
    retention REAL,
    next_revision_hours REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 🛠 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## Database

* SQLite

## Machine Learning

* Scikit-Learn
* XGBoost
* Pandas
* NumPy

## API

* FastAPI

---

# ▶ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ML-based-approach-to-Ebbinghaus-forgetting-curve.git

cd ML-based-approach-to-Ebbinghaus-forgetting-curve
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Linux/Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Streamlit App

```bash
streamlit run app.py
```

---

# ▶ Run FastAPI

```bash
uvicorn api:app --reload
```

---

# 📈 Research Motivation

This project is inspired by Hermann Ebbinghaus's Forgetting Curve, which explains how memory decays over time without revision.

Instead of using static revision schedules, this project uses Machine Learning to create personalized revision recommendations based on learner behavior.

---

# 🎯 Future Improvements

* Mobile Application
* Cloud Deployment
* Email Revision Reminders
* Push Notifications
* Real Student Data Integration
* Adaptive Difficulty Detection
* AI Study Coach
* Multi-User Analytics

---

# 👨‍💻 Author

Harihara Suthan

Computer Science Engineering Student

Passionate about:

* Machine Learning
* Data Science
* Learning Systems
* Educational Technology

---

# ⭐ If you find this project useful

Consider giving the repository a star and sharing feedback.
