from conversion_value import ObtainingCurrencyQuotes
from contextlib import nullcontext as does_not_raises
from typing import Optional
import pytest


class TestReceiptConversionValue:
    @pytest.mark.parametrize("currency_from, currency_to, conversion_date ,expected_result, expectation",
                             [
                                 ("USD", "RUB", "10.01.2025", 101.9166460968, does_not_raises()),
                                 ("USD", "RUB", "01.01.2000", 27.48314, does_not_raises()),
                             ]
                             )
    def test_get_conversion_value(self, currency_from: str, currency_to: str,
                                  conversion_date: str, expected_result: Optional[str], expectation) -> None:
        with expectation:
            assert ObtainingCurrencyQuotes(currency_from=currency_from, currency_to=currency_to,
                                           conversion_date=conversion_date).get_conversion_value() == expected_result