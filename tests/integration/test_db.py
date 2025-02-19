from contextlib import nullcontext as does_not_raise
from typing import Optional
import pytest
from db import Storage


@pytest.fixture(scope="function", autouse=True)
def test_db():
    """Creates a temporary SQLite database in memory and passes it to the test"""
    db = Storage(":memory:")  # Using an in-memory base
    yield db
    db.close()


class TestDB:
    @pytest.mark.parametrize("currency_from, currency_to, conversion_date, expected_result, expectation",
                             [
                                 ("USD", "RUB", "15.02.2025", 91.34, does_not_raise()),
                                 ("EUR", "IDR", "13.02.2025", 17015.54, does_not_raise()),
                                 ("RUB", "USD", "14.02.2025", None, does_not_raise()),
                                 ("RUB", "EUR", "13.02.2025", None, does_not_raise()),
                             ]
                             )
    # expected_result is responsible for what the result of the operation should be, i.e. return
    # In this case it is:
    # Float - if the record already exists in the database
    # None - if there is no record on the request in the database

    def test_add_and_get(
            self,
            test_db: Storage,
            currency_from: str,
            currency_to: str,
            conversion_date: str,
            expected_result: Optional[str],
            expectation
    ) -> None:
        with expectation:
            test_db.add(
                currency_from="USD",
                currency_to="RUB",
                conversion_date="15.02.2025",
                conversion_value=91.34
            )
            test_db.add(
                currency_from="EUR",
                currency_to="IDR",
                conversion_date="13.02.2025",
                conversion_value=17015.54
            )
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
                                 ("RUB", "USD", "14.02.2025", False, does_not_raise()),
                                 ("RUB", "EUR", "13.02.2025", False, does_not_raise()),
                             ]
                             )
    # expected_result in this case it is:
    # True - if a similar record is in the database;
    # False - if there is no similar record

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
            test_db.add(
                currency_from="USD",
                currency_to="RUB",
                conversion_date="15.02.2025",
                conversion_value=91.34
            )
            test_db.add(
                currency_from="EUR",
                currency_to="IDR",
                conversion_date="13.02.2025",
                conversion_value=17015.54
            )
            result = test_db.exists(
                currency_from=currency_from,
                currency_to=currency_to,
                conversion_date=conversion_date,
            )
            assert result == expected_result
