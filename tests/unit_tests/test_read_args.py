from args_validator.validator import ArgsValidator
from contextlib import nullcontext as does_not_raise
from typing import Optional
import pytest
import click


class TestArgsValidator:
    """Validity test for currency_to"""

    @pytest.mark.parametrize("ctx, param, currency_from, expected_result, expectation",
                             [
                                 (None, None, "1", None, pytest.raises(click.BadParameter)),
                                 (None, None, "usd", "USD", does_not_raise()),
                                 (None, None, "UDDD", None, pytest.raises(click.BadParameter)),
                                 (None, None, "EUR", "EUR", does_not_raise()),
                             ]
                             )
    def test_currency_from(self, ctx: click.Context, param: click.Option, currency_from: str,
                           expected_result: Optional[str], expectation):
        with expectation:
            assert ArgsValidator.validate_currency_from(ctx=ctx,
                                                        param=param,
                                                        currency_from=currency_from) == expected_result

    """Validity test for currency_to"""

    @pytest.mark.parametrize("ctx, param, currency_to, expected_result, expectation",
                             [
                                 (None, None, "1", None, pytest.raises(click.BadParameter)),
                                 (None, None, "usd", "USD", does_not_raise()),
                                 (None, None, "UDDD", None, pytest.raises(click.BadParameter)),
                                 (None, None, "EUR", "EUR", does_not_raise()),
                             ]
                             )
    def test_currency_to(self, ctx: click.Context, param: click.Option, currency_to: str,
                         expected_result: Optional[str], expectation):
        with expectation:
            assert ArgsValidator.validate_currency_to(ctx=ctx,
                                                      param=param,
                                                      currency_to=currency_to) == expected_result

    """Validity test for output_channel"""

    @pytest.mark.parametrize("ctx, param, output_channel, expected_result ,expectation",
                             [
                                 (None, None, "1", None, pytest.raises(click.BadParameter)),
                                 (None, None, "File", "file", does_not_raise()),
                                 (None, None, "FILEE", None, pytest.raises(click.BadParameter)),
                                 (None, None, "Terminall", None, pytest.raises(click.BadParameter)),
                             ]
                             )
    def test_output_channel(self, ctx: click.Context, param: click.Option, output_channel: str, expected_result,
                            expectation):
        with expectation:
            assert ArgsValidator.validate_output_channel(ctx=ctx,
                                                         param=param,
                                                         output_channel=output_channel) == expected_result

    """Validity test for identity_check"""

    @pytest.mark.parametrize("currency_from, currency_to, expected_result ,expectation",
                             [
                                 ("usd", "eur", None, does_not_raise()),
                                 ("usd", "USd", None, pytest.raises(click.BadParameter)),
                                 ("Rub", "EUR", None, does_not_raise()),
                                 ("rub", "RuB", None, pytest.raises(click.BadParameter)),
                             ]
                             )
    def test_identity_check(self, currency_from: str, currency_to: str, expectation, expected_result):
        with expectation:
            assert ArgsValidator.identity_check(currency_from=currency_from,
                                                currency_to=currency_to) == expected_result
