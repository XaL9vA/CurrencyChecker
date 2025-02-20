from typing import Dict
from json import loads as json_loads
import requests


class CurrenciesConverter:
    def __init__(self, api_key: str) -> None:
        self.__API_KEY: str = api_key

    def convert(self, currency_from: str, currency_to: str, conversion_date: str) -> float:
        conversion_date: str = self.__correct_date_format(conversion_date=conversion_date)
        params: Dict[str, str] = {
            "apikey": self.__API_KEY,
            "date": conversion_date,
            "base_currency": currency_from,
            "currencies": currency_to
        }
        with requests.Session() as local_session:
            try:
                response: requests.Response = local_session.get(
                    "https://app.freecurrencyapi.com/dashboard",
                    timeout=3)
                if response.ok:
                    api_response: requests.Response = local_session.get(
                        "https://api.freecurrencyapi.com/v1/historical",
                        timeout=5,
                        params=params
                    )
                    return json_loads(api_response.text)["data"][conversion_date][currency_to]
                else:
                    print(f"Error - {response.status_code}")
            except requests.exceptions.Timeout:
                print("Connection error, try again later")
            except requests.exceptions.RequestException as exception:
                print(f"Oops, something went wrong: {exception}")

    @staticmethod
    def __correct_date_format(conversion_date: str) -> str:
        """Necessary to convert the date to the format yyyy-mm-dd"""
        conversion_date = conversion_date.split(".")
        conversion_date = f"{conversion_date[2]}-{conversion_date[1]}-{conversion_date[0]}"
        return conversion_date
