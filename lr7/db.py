import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_suffix(".db")


def get_connection():
    """Return a new connection to the SQLite database."""

    return sqlite3.connect(DB_PATH)


def init_db():
    """Create base schema if it does not exist."""

    from .create_tables import create_tables

    create_tables()


if __name__ == "__main__":  # simple manual init
    init_db()
