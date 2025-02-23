from typing import Optional
import pytest
from dto import ViewDTO
from view import TerminalOutput, FileOutput


class TestView:
    @pytest.mark.parametrize("currency_from, currency_to, conversion_date, conversion_value, expected_result",
                             [
                                 ("USD", "RUB", "21.02.2025", 88.54366, None),
                                 ("RUB", "USD", "21.02.2025", 0.011, None)
                             ]
                             )
    def test_terminal_output(
            self,
            currency_from: str,
            currency_to: str,
            conversion_date: str,
            conversion_value: float,
            expected_result: None
    ) -> None:
        view_args: ViewDTO = ViewDTO(
            currency_from=currency_from,
            currency_to=currency_to,
            conversion_date=conversion_date,
            conversion_value=conversion_value
        )
        terminal_view = TerminalOutput()

        assert terminal_view.view(view_args=view_args) == expected_result

    @pytest.mark.parametrize("currency_from, currency_to, conversion_date, conversion_value, expected_result",
                             [
                                 ("USD", "RUB", "21.02.2025", 88.54366, None),
                                 ("RUB", "USD", "21.02.2025", 0.011, None),
                                 ("USD", "RUB", "21.02.2025", 88.54366, None),
                                 ("RUB", "USD", "21.02.2025", 0.011, None)
                             ]
                             )
    def test_file_output(
            self,
            currency_from: str,
            currency_to: str,
            conversion_date: str,
            conversion_value: float,
            expected_result: Optional[bool],
            tmp_path
    ) -> None:
        tmp_file = tmp_path / "test_history.csv"

        view_args: ViewDTO = ViewDTO(
            currency_from=currency_from,
            currency_to=currency_to,
            conversion_date=conversion_date,
            conversion_value=conversion_value
        )

        file_output = FileOutput(str(tmp_file))

        assert file_output.view(view_args) == expected_result
