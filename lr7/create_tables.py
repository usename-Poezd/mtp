from .db import get_connection


def create_tables():
    """Create several tables in the SQLite database.

    Tables:
      - departments(id, name)
      - employees(id, name, salary, department_id)
    """

    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS departments (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT NOT NULL,
                salary        REAL NOT NULL,
                department_id INTEGER REFERENCES departments(id)
            )
            """
        )

        conn.commit()


if __name__ == "__main__":
    create_tables()
