import click
from dto import CLIArgs
from args_validator import ArgsValidator


@click.command()
@click.option(
    "--conversion_date",
    required=True,
    type=str,
    prompt="----------------------------------------------------------------------------\n"
           "Enter the date in the format - day.month.year\n"
           "Example: 10.10.2010\n"
           "The date cannot be less than 01.01.1990\n"
           "Input",
    help="Records the date of conversion",
    callback=ArgsValidator.validate_conversion_date
)
@click.option(
    "--currency_from",
    required=True,
    type=str,
    prompt="----------------------------------------------------------------------------\n"
           "Currency for conversion",
    help="Enter the name of the currency you want to convert to another currency",
    callback=ArgsValidator.validate_currency_from
)
@click.option(
    "--currency_to",
    required=True,
    type=str,
    prompt="----------------------------------------------------------------------------\n"
           "Currency to which conversion takes place",
    help="Enter the currency to which you want to convert the currency entered in the previous step",
    callback=ArgsValidator.validate_currency_to
)
@click.option(
    "--output_channel",
    required=True,
    type=str,
    prompt="----------------------------------------------------------------------------\n"
           "Select the method of information output (By Digit) where:\n"
           "Terminal\n"
           "File\nYour choice",
    callback=ArgsValidator.validate_output_channel
)
def read_args(
        conversion_date: str,
        currency_from: str,
        currency_to: str,
        output_channel: str
) -> CLIArgs:
    try:
        ArgsValidator.identity_check(
            currency_from,
            currency_to
        )
    except click.BadParameter:
        print("-------------------------------------------------------------------\n"
              "Error: Currencies for conversion cannot be the same, please return")
    else:
        return CLIArgs(
            conversion_date=conversion_date,
            currency_from=currency_from,
            currency_to=currency_to,
            output_channel=output_channel
        )
