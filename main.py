from greetings import greetings
from dto import CLIArgs
from read_args import read_args
from conversion_value import CurrenciesConverter
from config import config


def main():
    greetings()
    args: CLIArgs = read_args(standalone_mode=False)

    currency_converter = CurrenciesConverter(config.api_key)
    conversion_value: float = currency_converter.convert(
        conversion_date=args.conversion_date,
        currency_from=args.currency_from,
        currency_to=args.currency_to
    )


if __name__ == '__main__':
    main()
