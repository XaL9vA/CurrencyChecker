from typing import Optional
from contextlib import nullcontext as does_not_raise
import pytest
from converter import CurrenciesConverter
from config import config

class TestReceiptConversionValue:
    @pytest.mark.parametrize("currency_from, currency_to, conversion_date ,expected_result, expectation",
                             [
                                 ("USD", "RUB", "10.01.2025", 101.9166460968, does_not_raise()),
                                 ("USD", "RUB", "01.01.2000", 27.48314, does_not_raise()),
                             ]
                             )
    def test_get_conversion_value(
            self, currency_from: str,
            currency_to: str,
            conversion_date: str,
            expected_result: Optional[str],
            expectation
    ) -> None:
        with expectation:
            currency_converter = CurrenciesConverter(api_key=config.api_key)
            assert currency_converter.convert(currency_from=currency_from,
                                              currency_to=currency_to,
                                              conversion_date=conversion_date
                                              ) == expected_result
