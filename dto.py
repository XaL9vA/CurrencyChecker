from dataclasses import dataclass


@dataclass(frozen=True)
class CLIArgs:
    currency_from: str
    currency_to: str
    conversion_date: str
    output_channel: str


@dataclass(frozen=True)
class DBColumns:
    currency_from: str
    currency_to: str
    conversion_date: str
    conversion_result: float