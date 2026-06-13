CREATE TABLE users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password TEXT
);

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