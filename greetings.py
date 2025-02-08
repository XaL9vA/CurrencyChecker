from args_validator import CURRENCY_VALID
from typing import List


def greetings() -> None:
    print("Hi user, this program converts currencies\n"
          "Here is the current list:\n"
          "-------------------------------------------")
    valid_currencies: List[str] = list(CURRENCY_VALID)
    max_currency_for_line: int = 10
    for currency in range(0, len(valid_currencies), max_currency_for_line):
        line: str = " ".join(valid_currencies[currency:currency + max_currency_for_line])
        print(line)
