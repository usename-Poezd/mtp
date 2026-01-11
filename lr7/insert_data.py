from .db import get_connection


def insert_sample_data():
    """Insert several rows into the tables."""

    with get_connection() as conn:
        cur = conn.cursor()

        # ensure base tables exist
        from .create_tables import create_tables

        create_tables()

        departments = [
            ("IT",),
            ("HR",),
            ("Finance",),
        ]

        cur.executemany(
            "INSERT OR IGNORE INTO departments(name) VALUES (?)",
            departments,
        )

        employees = [
            ("Alice", 150000, "IT"),
            ("Bob", 120000, "IT"),
            ("Carol", 100000, "HR"),
            ("Dave", 130000, "Finance"),
        ]

        for name, salary, dep_name in employees:
            cur.execute("SELECT id FROM departments WHERE name = ?", (dep_name,))
            row = cur.fetchone()
            if row is None:
                continue
            department_id = row[0]
            cur.execute(
                """
                INSERT INTO employees(name, salary, department_id)
                VALUES (?, ?, ?)
                """,
                (name, salary, department_id),
            )

        conn.commit()


if __name__ == "__main__":
    insert_sample_data()
