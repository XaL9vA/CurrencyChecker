from abc import ABC, abstractmethod
from dto import ViewDTO
from typing import Optional


class Output(ABC):
    @abstractmethod
    def view(self, view_args: ViewDTO) -> None:
        pass


class TerminalOutput(Output):
    def view(self, view_args: ViewDTO) -> None:
        print(
            "--------------------------------------------------\n"
           f"Conversion date - {view_args.conversion_date}\n"
           f"One {view_args.currency_from} equals {view_args.conversion_value} {view_args.currency_to}\n"
            "--------------------------------------------------\n"
        )


class FileOutput(Output):
    def __init__(self, filename: str):
        self.__filename: str = filename

    def view(self, view_args: ViewDTO) -> Optional[bool]:
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                entry: str = (
                f"Conversion date - {view_args.conversion_date}\n"
                f"One {view_args.currency_from} equals {view_args.conversion_value} {view_args.currency_to}\n"
                "--------------------------------------------------\n"
            )
                if entry in file.read():
                    return

        except FileNotFoundError:
            pass

        try:
            with open(self.__filename, "a", encoding="utf-8") as file:
                file.write(
                    f"Conversion date - {view_args.conversion_date}\n"
                    f"One {view_args.currency_from} equals {view_args.conversion_value} {view_args.currency_to}\n"
                    "--------------------------------------------------\n"
                )

        except Exception as er:
            print(f"ERROR - {er}")
