from contextlib import nullcontext as does_not_raise
from typing import Optional
import pytest
from db import Storage


@pytest.fixture(scope="function", autouse=True)
def test_db():
    db = Storage(":memory:")  # temporary SQLite database
    data = [
        ("USD", "RUB", "15.02.2025", 91.34),
        ("EUR", "IDR", "13.02.2025", 17015.54),
        ("RUB", "USD", "14.02.2025", 0.011),
        ("RUB", "EUR", "13.02.2025", 0.0107),
    ]
    for entry in data:
        db.add(
            currency_from=entry[0],
            currency_to=entry[1],
            conversion_date=entry[2],
            conversion_value=entry[3]
        )
    yield db
    db.close()


class TestDB:
    @pytest.mark.parametrize("currency_from, currency_to, conversion_date, expected_result, expectation",
                             [
                                 ("USD", "RUB", "15.02.2025", (91.34,), does_not_raise()),
                                 ("EUR", "IDR", "13.02.2025", (17015.54,), does_not_raise()),
                                 ("RUB", "THB", "14.02.2025", None, does_not_raise()),
                                 ("RUB", "GBP", "13.02.2025", None, does_not_raise()),
                             ]
                             )
    def test_get(
            self,
            test_db: Storage,
            currency_from: str,
            currency_to: str,
            conversion_date: str,
            expected_result: Optional[str],
            expectation
    ) -> None:
        with expectation:
            result = test_db.get(
                currency_from=currency_from,
                currency_to=currency_to,
                conversion_date=conversion_date
            )
            assert result == expected_result

    @pytest.mark.parametrize("currency_from, currency_to, conversion_date, expected_result, expectation",
                             [
                                 ("USD", "RUB", "15.02.2025", True, does_not_raise()),
                                 ("EUR", "IDR", "13.02.2025", True, does_not_raise()),
                                 ("RUB", "THB", "12.01.2025", False, does_not_raise()),
                                 ("RUB", "GBP", "10.01.2025", False, does_not_raise()),
                             ]
                             )
    def test_exists(
            self,
            test_db: Storage,
            currency_from: str,
            currency_to: str,
            conversion_date: str,
            expected_result: Optional[str],
            expectation
    ) -> None:
        with expectation:
            result = test_db.exists(
                currency_from=currency_from,
                currency_to=currency_to,
                conversion_date=conversion_date,
            )
            assert result == expected_result
