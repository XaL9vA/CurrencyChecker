from typing import List
from args_validator import CURRENCIES


def greetings() -> None:
    print("Hi user, this program converts currencies\n"
          "Here is the current list:\n"
          "-------------------------------------------")
    valid_currencies: List[str] = sorted(list(CURRENCIES))
    max_currency_for_line: int = 15
    for currency in range(0, len(valid_currencies), max_currency_for_line):
        line: str = " ".join(valid_currencies[currency:currency + max_currency_for_line])
        print(line)
