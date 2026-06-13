import sqlite3
import pandas as pd

# --------------------------------

# Database Connection

# --------------------------------

def get_connection():


    conn = sqlite3.connect(
        "memory_retention.db",
        check_same_thread=False
    )

    return conn


# --------------------------------

# Topic Information

# --------------------------------

def get_topic_info(topic_name):


    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            nth_revision,
            created_at
        FROM study_sessions
        WHERE topic_name = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (topic_name,)
    )

    result = cursor.fetchone()

    conn.close()

    return result


# --------------------------------

# Topic History

# --------------------------------

def get_topic_history(topic_name):

    conn = get_connection()

    query = """
    SELECT
        nth_revision,
        retention,
        next_revision_hours,
        created_at
    FROM study_sessions
    WHERE topic_name = ?
    ORDER BY nth_revision
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(topic_name,)
    )

    conn.close()

    return df

# --------------------------------

# Save Study Session

# --------------------------------

def save_session(
    topic_name,
    revision_timing,
    nth_revision,
    sleep_duration,
    topic_difficulty,
    study_duration,
    retention,
    next_revision_hours
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO study_sessions(

    topic_name,
    revision_timing,
    nth_revision,
    sleep_duration,
    topic_difficulty,
    study_duration,
    retention,
    next_revision_hours

)

VALUES(?,?,?,?,?,?,?,?)
        """,
        (
    topic_name,
    revision_timing,
    nth_revision,
    sleep_duration,
    topic_difficulty,
    study_duration,
    retention,
    next_revision_hours
)
    )

    conn.commit()

    conn.close()

# --------------------------------

# Latest Session

# --------------------------------

def get_latest_session():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            retention,
            next_revision_hours
        FROM study_sessions
        ORDER BY id DESC
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    conn.close()

    return row

# --------------------------------

# Dashboard Metrics

# --------------------------------

def get_total_sessions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM study_sessions"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count

def get_average_retention():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT AVG(retention) FROM study_sessions"
    )

    avg = cursor.fetchone()[0]

    conn.close()

    return avg if avg else 0

# --------------------------------

# Analytics

# --------------------------------

def get_all_sessions():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM study_sessions
        ORDER BY id
        """,
        conn
    )

    conn.close()

    return df

# --------------------------------

# Revision Planner

# --------------------------------

def get_revision_schedule():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            topic_name,
            next_revision_hours,
            created_at
        FROM study_sessions
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows

# --------------------------------

# Authentication

# --------------------------------

def create_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users(
                username,
                password
            )
            VALUES(?,?)
            """,
            (username, password)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user
