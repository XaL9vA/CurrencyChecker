import sqlite3

from typing import Tuple, Optional


class Storage:
    def __init__(self, dsn: str) -> None:
        self.__session: sqlite3.Connection = sqlite3.connect(dsn)
        self.__cursor: sqlite3.Cursor = self.__session.cursor()
        self.__create_tables()

    def get(self, currency_from: str, currency_to: str, conversion_date: str) -> float:
        with self.__session:
            self.__cursor.execute("""
                SELECT conversion_value FROM currencies_history
                WHERE currency_from = ? AND currency_to = ? AND conversion_date = ?
                """, (currency_from, currency_to, conversion_date))

            row: Optional[Tuple[float]] = self.__cursor.fetchone()
            if row is None:
                raise ValueError("Conversion not found")

            return float(row[0])

    def add(self, currency_from: str, currency_to: str, conversion_date: str, conversion_value: float) -> None:
        with self.__session:
            self.__cursor.execute("""
                INSERT INTO currencies_history (
                currency_from,
                currency_to,
                conversion_date,
                conversion_value
                )
                VALUES (?, ?, ?, ?)
                """, (currency_from, currency_to, conversion_date, conversion_value))

            self.__session.commit()
            print("A new entry has been added")

    def exists(self, currency_from: str, currency_to: str, conversion_date: str) -> bool:
        with self.__session:
            self.__cursor.execute("""
                SELECT 1 FROM currencies_history
                WHERE currency_from = ? AND currency_to = ? AND conversion_date = ?
                """, (currency_from, currency_to, conversion_date))

            if self.__cursor.fetchone():
                print("The record exists in the database")
                return True  # Returns if the record is found

            return False

    def close(self) -> None:
        """Safely closes the connection to the database"""
        if hasattr(self, '__cursor') and self.__cursor:
            self.__cursor.close()

        if hasattr(self, '__session') and self.__session:
            self.__session.close()
            print("Database connection closed")

    def __create_tables(self) -> None:
        with self.__session:
            self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS currencies_history(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_from TEXT NOT NULL,
                    currency_to TEXT NOT NULL,
                    conversion_date TEXT NOT NULL,
                    conversion_value REAL NOT NULL
                    )
                """)

    def __del__(self) -> None:
        self.close()
