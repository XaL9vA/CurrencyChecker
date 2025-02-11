from os import getenv
from dotenv import load_dotenv, find_dotenv
import requests
from json import loads


class ObtainingCurrencyQuotes:
    load_dotenv(find_dotenv())

    def __init__(self, currency_from: str, currency_to: str, conversion_date: str) -> None:
        """Necessary for correct output"""
        self.__currency_to: str = currency_to
        self.__conversion_date: str = self.correct_date_format(conversion_date)
        """Request parameters"""
        self.__params = {
            "apikey": getenv("API_KEY"),
            "date": self.__conversion_date,
            "base_currency": currency_from,
            "currencies": self.__currency_to
        }

    def get_conversion_value(self) -> float:
        with requests.Session() as local_session:
            try:
                response: requests.codes = local_session.get("https://app.freecurrencyapi.com/dashboard")
                if response.ok:
                    api_response: requests.Response = local_session.get(
                        "https://api.freecurrencyapi.com/v1/historical",
                        params=self.__params
                    )
                    return loads(api_response.text)["data"][f"{self.__conversion_date}"][f"{self.__currency_to}"]
                else:
                    print(f"Error - {response.status_code}")
            except requests.exceptions.RequestException as exception:
                print(f"Oops, something went wrong: {exception}")

    @staticmethod
    def correct_date_format(conversion_date: str) -> str:
        """Necessary to convert the date to the format yyyy-mm-dd"""
        conversion_date = conversion_date.split(".")
        conversion_date = f"{conversion_date[2]}-{conversion_date[1]}-{conversion_date[0]}"
        return conversion_date

