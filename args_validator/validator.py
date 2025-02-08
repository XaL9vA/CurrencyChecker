from .constants import CURRENCY_VALID, CURRENCY_OUTPUT
from datetime import datetime
import click


class ArgsValidator:

    @staticmethod
    def validate_conversion_date(ctx: click.Context, param: click.Option, conversion_date: str) -> str:
        try:
            conversion_date_format: datetime.date = datetime.strptime(conversion_date, "%d.%m.%Y")
            minimum_date_allowed: datetime.date = datetime.strptime("01.01.1990", "%d.%m.%Y")
        except ValueError:
            raise click.BadParameter(f"ValueError: your date is incorrect, please check")
        else:
            if conversion_date_format > datetime.now():
                raise click.BadParameter(f"the date cannot be greater than the current date")
            elif conversion_date_format < minimum_date_allowed:
                raise click.BadParameter(f"Your date cannot be less than 01.01.1990 :)")
            return conversion_date

    @staticmethod
    def validate_currency_from(ctx: click.Context, param: click.Option, currency_from: str) -> str:
        currency_from = currency_from.upper()
        if currency_from not in CURRENCY_VALID:
            raise click.BadParameter(f"{currency_from} does not exist in a valid list ")
        return currency_from

    @staticmethod
    def validate_currency_to(ctx: click.Context, param: click.Option, currency_to: str) -> str:
        currency_to = currency_to.upper()
        if currency_to not in CURRENCY_VALID:
            raise click.BadParameter(f"{currency_to} does not exist in a valid list")
        return currency_to

    @staticmethod
    def validate_output_channel(ctx: click.Context, param: click.Option, output_channel: str) -> str:
        output_channel = output_channel.lower()
        if output_channel not in CURRENCY_OUTPUT:
            raise click.BadParameter(f"{output_channel} does not exist in the allowed list of outputs")
        return output_channel

    @staticmethod
    def identity_check(currency_from: str, currency_to: str) -> None:
        if currency_from.upper() == currency_to.upper():
            raise click.BadParameter(f"Currencies for conversion cannot be the same")
