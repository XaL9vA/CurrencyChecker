import datetime
import click

from .constants import CURRENCIES, OUTPUT_CHANNELS


class ArgsValidator:

    @staticmethod
    def validate_conversion_date(
            ctx: click.Context,
            param: click.Option,
            conversion_date: str
    ) -> str:
        try:
            conversion_date_format: datetime.date = datetime.datetime.strptime(conversion_date, "%d.%m.%Y").date()
            minimum_date_allowed: datetime.date = datetime.datetime.strptime("01.01.2000", "%d.%m.%Y").date()
            date_today: datetime.date = datetime.datetime.now().date()
        except ValueError:
            raise click.BadParameter("ValueError: your date is incorrect, please check")

        if conversion_date_format > date_today:
            raise click.BadParameter("the date cannot be greater than the current date")
        elif conversion_date_format == date_today:
            raise click.BadParameter("The date can't be “today,” only the previous date")
        elif conversion_date_format < minimum_date_allowed:
            raise click.BadParameter("Your date cannot be less than 01.01.2000 :)")
        return conversion_date

    @staticmethod
    def validate_currency_from(
            ctx: click.Context,
            param: click.Option,
            currency_from: str
    ) -> str:
        currency_from = currency_from.upper()
        if currency_from not in CURRENCIES:
            raise click.BadParameter(f"{currency_from} does not exist in a valid list ")
        return currency_from

    @staticmethod
    def validate_currency_to(
            ctx: click.Context,
            param: click.Option,
            currency_to: str,
    ) -> str:
        currency_to = currency_to.upper()
        if currency_to not in CURRENCIES:
            raise click.BadParameter(f"{currency_to} does not exist in a valid list")
        """A double check is performed by calling the parameter currency_from"""
        currency_from: str = str(ctx.params.get("currency_from"))
        ArgsValidator.identity_check(currency_from=currency_from, currency_to=currency_to)
        return currency_to

    @staticmethod
    def validate_output_channel(
            ctx: click.Context,
            param: click.Option,
            output_channel: str
    ) -> str:
        output_channel = output_channel.lower()
        if output_channel not in OUTPUT_CHANNELS:
            raise click.BadParameter(f"{output_channel} does not exist in the allowed list of outputs")
        return output_channel

    @staticmethod
    def identity_check(
            currency_from: str,
            currency_to: str
    ) -> None:
        if currency_from.upper() == currency_to.upper():
            raise click.BadParameter("Currencies for conversion cannot be the same")
