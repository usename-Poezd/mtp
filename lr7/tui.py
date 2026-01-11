"""Simple text UI for working with the SQLite database."""

from textwrap import dedent

from .create_tables import create_tables
from .insert_data import insert_sample_data
from .update_data import update_employee_salary
from .db import init_db, get_connection


def print_header(title: str) -> None:
    print("=" * 50)
    print(title)
    print("=" * 50)


def action_create_tables() -> None:
    create_tables()
    print("Таблицы успешно созданы (если их не было).")


def action_insert_data() -> None:
    insert_sample_data()
    print("Тестовые данные вставлены.")


def action_update_record() -> None:
    try:
        employee_id = int(input("Введите ID сотрудника: "))
        new_salary = float(input("Введите новую зарплату: "))
    except ValueError:
        print("Ошибка: ID и зарплата должны быть числами.")
        return

    affected = update_employee_salary(employee_id, new_salary)
    if affected:
        print(f"Обновлено записей: {affected}")
    else:
        print("Запись с таким ID не найдена.")


def action_show_data() -> None:
    with get_connection() as conn:
        cur = conn.cursor()

        print_header("Таблица departments")
        for row in cur.execute("SELECT id, name FROM departments ORDER BY id"):
            print(row)

        print_header("Таблица employees")
        for row in cur.execute(
            """
            SELECT e.id, e.name, e.salary, d.name as department
            FROM employees e
            LEFT JOIN departments d ON e.department_id = d.id
            ORDER BY e.id
            """
        ):
            print(row)


def main() -> None:
    init_db()

    while True:
        print_header("LR7 - SQLite TUI")
        print(
            dedent(
                """
                Выберите действие:
                  1. Создать таблицы
                  2. Вставить тестовые данные
                  3. Обновить запись (зарплата сотрудника)
                  4. Показать содержимое таблиц
                  0. Выход
                """
            )
        )

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            action_create_tables()
        elif choice == "2":
            action_insert_data()
        elif choice == "3":
            action_update_record()
        elif choice == "4":
            action_show_data()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неизвестная команда.")

        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()
