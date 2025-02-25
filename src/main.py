from typing import Optional

from src.greetings import greetings
from src.dto import CLIArgs, ViewDTO
from src.read_args import read_args
from src.converter import CurrenciesConverter
from src.config import config, VIEW_CHANNELS_MAP, VIEW_CHANNELS_ARGS_MAP
from src.db import Storage
from src.view import View


def main():
    greetings()

    args: CLIArgs = read_args(standalone_mode=False)

    db: Storage = config.db_name
    exists = db.exists(
        currency_from=args.currency_from,
        currency_to=args.currency_to,
        conversion_date=args.conversion_date
    )

    conversion_value: float
    if exists:
        db_conversion_value: Optional[float] = db.get(
            currency_from=args.currency_from,
            currency_to=args.currency_to,
            conversion_date=args.conversion_date
        )

        assert db_conversion_value is not None
        conversion_value = db_conversion_value
    else:
        converter = CurrenciesConverter(config.api_key)
        conversion_value = converter.convert(
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

    view_args: ViewDTO = ViewDTO(
        currency_from=args.currency_from,
        currency_to=args.currency_to,
        conversion_date=args.conversion_date,
        conversion_value=conversion_value
    )

    view: View = VIEW_CHANNELS_MAP[args.output_channel](**VIEW_CHANNELS_ARGS_MAP[args.output_channel])
    view.view(view_args=view_args)


if __name__ == '__main__':
    main()
