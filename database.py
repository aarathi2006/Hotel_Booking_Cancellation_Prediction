import sqlite3

DATABASE = "database.db"

def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        fullname TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)

    # Predictions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        lead_time INTEGER,

        arrival_date_day_of_month INTEGER,

        arrival_date_week_number INTEGER,

        stays_in_weekend_nights INTEGER,

        stays_in_week_nights INTEGER,

        adr REAL,

        adults INTEGER,

        agent INTEGER,

        total_of_special_requests INTEGER,

        prediction TEXT,

        probability REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id) REFERENCES users(id)

    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database Created Successfully!")
