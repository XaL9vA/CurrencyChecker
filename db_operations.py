import sqlite3
from typing import Optional, Union


class DBOperations:
    def __init__(self, connection: str) -> None:
        """Инициализация возвращаемых данных об операции"""
        self.__data_tuple: Optional[tuple[str, float]] = None

        try:
            self.__session: sqlite3.Connection = sqlite3.connect(connection)
            self.__cursor: sqlite3.Cursor = self.__session.cursor()
            # Процесс создания таблицы (Либо проверки, существует ли таблица)
            self.__create_table()
        except sqlite3.Error as er:
            print(f"ERROR - {er}")
            raise

    """Приватный метод, необходим для создания таблицы в Базе Данных"""

    def __create_table(self) -> None:
        with self.__session:
            self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS CurrencyCheckerOperations (
                    OperationID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Currency_from TEXT NOT NULL,
                    Currency_to TEXT NOT NULL,
                    Conversion_date TEXT NOT NULL,
                    Conversion_result REAL NOT NULL
                    )
                """)

    """Используется для: Проверки на наличие идентичной записи / Сохранения записи в Базе Данных"""

    def save(self, currency_from: str, currency_to: str, conversion_date: str, conversion_result: float
             ) -> Union[tuple[str, float], False]:
        try:
            with self.__session:

                """Проверка на существования идентичной записи"""
                self.__cursor.execute("""
            SELECT 1 FROM CurrencyCheckerOperations
            WHERE Currency_from = ? AND Currency_to = ? AND Conversion_date = ?
            """, (currency_from, currency_to, conversion_date))

                """Блок срабатывает, если из SQL-Запроса SELECT возвращается кортеж - (1,)"""
                """То есть аналогичная запись уже существует в таблице"""
                if self.__cursor.fetchone():
                    return False

                """Если SQL-Запрос возвращает None (т.е идентичная запись не найдена), то выполняется инструкция:"""
                self.__cursor.execute("""   
                INSERT INTO CurrencyCheckerOperations (
                Currency_from, 
                Currency_to, 
                Conversion_date, 
                Conversion_result
                )
                VALUES (?, ?, ?, ?)
                """, (currency_from, currency_to, conversion_date, conversion_result))

                self.__session.commit()
                print("A new entry has been added / Добавлена новая запись")

                """Записываем аргументы для вывода в необходимый канал"""
                self.__data_tuple = (currency_from, currency_to, conversion_date, conversion_result)

        except sqlite3.Error as er:
            print(f"ERROR - {er}")
            raise

    """Используется для получения записи с Базы Данных"""

    def record_availability(self, currency_from: str, currency_to: str, conversion_date: str
                            ) -> Union[tuple[str, float], False]:
        try:
            with self.__session:

                self.__cursor.execute("""
            SELECT Currency_from, Currency_to, Conversion_date, Conversion_result FROM CurrencyCheckerOperations
            WHERE Currency_from = ? AND Currency_to = ? AND Conversion_date = ?
            """, (currency_from, currency_to, conversion_date))

                """Используется для проверки возврата данных"""
                row_checker = self.__cursor.fetchone()
                if row_checker is None:
                    "Record not found / Запись не найдена"
                    return False

                """Записываем аргументы для вывода в необходимый канал"""
                self.__data_tuple = row_checker

        except sqlite3.Error as er:
            print(f"ERROR - {er}")
            raise

    """Используется для получения кортежа значений с БД"""

    def data_retrieval(self) -> Union[tuple[str, float]]:
        return self.__data_tuple

    def close_session(self) -> None:
        """Используется для безопасного закрытия соединения"""
        try:
            if hasattr(self, '__cursor') and self.__cursor:
                self.__cursor.close()
            if hasattr(self, '__session') and self.__session:
                self.__session.close()
                self.__session = None
                print("Database connection closed / Соединение с БД закрыто")
        except sqlite3.Error as er:
            print(f"ERROR closing DB: {er}")
            raise

    def __del__(self) -> None:
        """Используется в случае уничтожения объекта"""
        self.close_session()
