import sqlite3
from typing import Optional, Tuple
from dto import DBColumns


class Storage:
    def __init__(self, dsn: str) -> None:
        self.__session: sqlite3.Connection = sqlite3.connect(dsn)
        self.__cursor: sqlite3.Cursor = self.__session.cursor()
        self.__create_tables()

    def get(self, currency_from: str, currency_to: str, conversion_date: str) -> Optional[DBColumns]:
        """Writes values for subsequent manipulations to the dataclass"""
        with self.__session:
            self.__cursor.execute("""
                SELECT currency_from, currency_to, conversion_date, conversion_result FROM currencies_history
                WHERE currency_from = ? AND currency_to = ? AND conversion_date = ?
                """, (currency_from, currency_to, conversion_date))
            row: Optional[Tuple[str, str, str, float]] = self.__cursor.fetchone()
            if row is None:
                return None
            return DBColumns(
                currency_from=row[0],
                currency_to=row[1],
                conversion_date=row[2],
                conversion_result=row[3]
            )

    def add(self, currency_from: str, currency_to: str, conversion_date: str, conversion_result: float) -> None:
        """Adds a new row to an operation in the table"""
        with self.__session:
            self.__cursor.execute("""   
                INSERT INTO currencies_history (
                currency_from, 
                currency_to, 
                conversion_date, 
                conversion_result
                )
                VALUES (?, ?, ?, ?)
                """, (currency_from, currency_to, conversion_date, conversion_result))
            self.__session.commit()
            print("A new entry has been added")

    def exists(self, currency_from: str, currency_to: str, conversion_date: str) -> bool:
        """Checking for the existence of similar records in the database"""
        with self.__session:
            self.__cursor.execute("""
                SELECT 1 FROM currencies_history
                WHERE currency_from = ? AND currency_to = ? AND conversion_date = ?
                """, (currency_from, currency_to, conversion_date))

            if self.__cursor.fetchone():
                return True  # Returns if the record is found
            return False

    def close(self) -> None:
        """Safely closes the connection to the database"""
        if hasattr(self, '__cursor') and self.__cursor:
            self.__cursor.close()
        if hasattr(self, '__session') and self.__session:
            self.__session.close()
            self.__session = None
            print("Database connection closed")

    def __create_tables(self) -> None:
        with self.__session:
            self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS currencies_history(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_from TEXT NOT NULL,
                    currency_to TEXT NOT NULL,
                    conversion_date TEXT NOT NULL,
                    conversion_result REAL NOT NULL
                    )
                """)

    def __del__(self) -> None:
        self.close()
