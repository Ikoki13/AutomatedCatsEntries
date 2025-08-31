from datetime import datetime, date
from unittest.mock import patch

from src.Helpers.dateHelper import get_formatted_date, calculate_date_difference


def test_get_formatted_date_default_date():
    with patch('builtins.input', return_value=''):
        result = get_formatted_date("Enter date: ")
        assert result.date() == date.today()


def test_get_formatted_date_valid_input():
    with patch('builtins.input', return_value='20.10.2023'):
        result = get_formatted_date("Enter date: ")
        assert result == datetime(2023, 10, 20, 0, 0)


def test_get_formatted_date_invalid_input(capsys):
    with patch('builtins.input', side_effect=['invalid_date', '21.10.2023']):
        result = get_formatted_date("Enter date: ")
        captured = capsys.readouterr()
        assert "❌ Invalid date format 'invalid_date'. Please use '%d.%m.%Y'." in captured.out
        assert result == datetime(2023, 10, 21, 0, 0)


def test_calculate_date_difference_positive():
    start_date = datetime(2023, 10, 10)
    end_date = datetime(2023, 10, 20)
    result = calculate_date_difference(start_date, end_date)
    assert result == 10


def test_calculate_date_difference_negative():
    start_date = datetime(2023, 10, 20)
    end_date = datetime(2023, 10, 10)
    result = calculate_date_difference(start_date, end_date)
    assert result == -10


def test_calculate_date_difference_same_date():
    start_date = datetime(2023, 10, 10)
    end_date = datetime(2023, 10, 10)
    result = calculate_date_difference(start_date, end_date)
    assert result == 0