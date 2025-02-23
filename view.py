from abc import ABC, abstractmethod
from dto import ViewDTO
import csv


class Output(ABC):
    @abstractmethod
    def view(self, view_args: ViewDTO) -> None:
        raise NotImplementedError


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

    def view(self, view_args: ViewDTO) -> None:
        columns = ["conversion_date", "currency_from", "currency_to", "conversion_value"]
        data = [
            view_args.conversion_date, view_args.currency_from,
            view_args.currency_to, str(view_args.conversion_value)
        ]

        reader = []

        try:
            with open(self.__filename, "r", newline="", encoding="utf-8") as file:
                reader = list(csv.reader(file))

                if data in reader:
                    return

        except FileNotFoundError:
            pass

        try:
            with open(self.__filename, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if columns in reader:
                    writer.writerow(data)
                    return

                else:
                    writer.writerow(columns)
                    writer.writerow(data)

        except Exception as er:
            print(f"ERROR - {er}")
