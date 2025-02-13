from dataclasses import dataclass


@dataclass(frozen=True)
class CLIArgs:
    currency_from: str
    currency_to: str
    conversion_date: str
    output_channel: str
