import csv

from typing import List, Dict, Any
from abc import ABC, abstractmethod

from src.dto import ViewDTO


class View(ABC):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def view(self, view_args: ViewDTO) -> None:
        raise NotImplementedError


class TerminalView(View):
    def view(self, view_args: ViewDTO) -> None:
        print(
            "--------------------------------------------------\n"
            f"Conversion date - {view_args.conversion_date}\n"
            f"One {view_args.currency_from} equals {view_args.conversion_value} {view_args.currency_to}\n"
            "--------------------------------------------------\n"
        )


class FileView(View):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        super().__init__(**kwargs)
        self.__filename: str = str(kwargs["filename"])

    def view(self, view_args: ViewDTO) -> None:
        headers: List[str] = ["conversion_date", "currency_from", "currency_to", "conversion_value"]
        data: List[str] = [
            view_args.conversion_date,
            view_args.currency_from,
            view_args.currency_to,
            str(view_args.conversion_value)
        ]

        entries: List[List[str]] = []
        try:
            with open(self.__filename, "r", newline="", encoding="utf-8") as file:
                entries: List[List[str]] = list(csv.reader(file))  # type: ignore[no-redef]

                if data in entries:
                    print("This record is already in the file")
                    return

        except FileNotFoundError:
            pass

        try:
            with open(self.__filename, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if headers not in entries:
                    writer.writerow(headers)

                writer.writerow(data)

        except Exception as er:
            print(f"ERROR - {er}")

# Comments like type: ignore[] are needed to ignore errors in mypy
# In particular, here:
# Line 40 - [no-redef] - we need to store the value of the variable outside the with manager
# in order to refer to it in another block
