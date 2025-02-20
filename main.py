from greetings import greetings
from dto import CLIArgs
from read_args import read_args
from converter import CurrenciesConverter
from config import config
from db import Storage


def main():
    greetings()

    args: CLIArgs = read_args(standalone_mode=False)

    db = Storage("currency_operations.db")
    exists = db.exists(
        currency_from=args.currency_from,
        currency_to=args.currency_to,
        conversion_date=args.conversion_date
    )
    if exists:
        conversion_value: float = db.get(
            currency_from=args.currency_from,
            currency_to=args.currency_to,
            conversion_date=args.conversion_date
        )
    else:
        converter = CurrenciesConverter(config.api_key)
        conversion_value: float = converter.convert(
            conversion_date=args.conversion_date,
            currency_from=args.currency_from,
            currency_to=args.currency_to
        )

        db.add(
            currency_from=args.currency_from,
            currency_to=args.currency_to,
            conversion_date=args.conversion_date,
            conversion_value=conversion_value
        )


if __name__ == '__main__':
    main()
