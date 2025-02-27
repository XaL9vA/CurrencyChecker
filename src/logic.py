from typing import Dict

from src.dto import CLIArgs, ViewDTO
from src.converter import CurrenciesConverter
from src.config import config, VIEW_MAP
from src.db import Storage
from src.view import View


class Logic:
    def __init__(
            self,
            storage: Storage,
            views_map: Dict[str, View]
    ) -> None:
        self.__storage: Storage = storage
        self.__views_map: Dict[str, View] = views_map

    def run(self, args: CLIArgs):
        if self.__storage.exists(
                currency_from=args.currency_from,
                currency_to=args.currency_to,
                conversion_date=args.conversion_date
        ):
            conversion_value: float = self.__storage.get(
                currency_from=args.currency_from,
                currency_to=args.currency_to,
                conversion_date=args.conversion_date
            )
        else:
            converter: CurrenciesConverter = CurrenciesConverter(config.api_key)
            conversion_value: float = converter.convert(  # type: ignore[no-redef]
                conversion_date=args.conversion_date,
                currency_from=args.currency_from,
                currency_to=args.currency_to
            )

        self.__storage.add(
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

        view: View = VIEW_MAP[args.output_channel]
        view.view(view_args=view_args)
