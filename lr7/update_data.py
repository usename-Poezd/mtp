from .db import get_connection


def update_employee_salary(employee_id: int, new_salary: float) -> int:
    """Update salary for the given employee id.

    Returns number of affected rows.
    """

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE employees SET salary = ? WHERE id = ?",
            (new_salary, employee_id),
        )
        conn.commit()
        return cur.rowcount


if __name__ == "__main__":
    # simple manual test
    print("Updated rows:", update_employee_salary(1, 200000))
