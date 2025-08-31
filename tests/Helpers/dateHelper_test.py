import os
import sys
from datetime import datetime, date, timezone
from unittest.mock import patch
import pytest
from src.Helpers.dateHelper import get_formatted_date, calculate_date_difference

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


class TestDateHelper:
    @patch('builtins.input', return_value='')
    def test_get_formatted_date_empty_input(self, mock_input):
        test_date = date(2023, 1, 1)
        result = get_formatted_date("Enter date:", test_date)
        
        assert isinstance(result, datetime)
        assert result.date() == test_date
        assert result.tzinfo == timezone.utc
        
    @patch('builtins.input', return_value='15.08.2023')
    def test_get_formatted_date_valid_input(self, mock_input):
        result = get_formatted_date("Enter date:")
        expected = datetime(2023, 8, 15)
        
        assert result == expected
        
    @patch('builtins.input', side_effect=['invalid', '15.08.2023'])
    def test_get_formatted_date_invalid_then_valid(self, mock_input):
        result = get_formatted_date("Enter date:")
        expected = datetime(2023, 8, 15)
        
        assert result == expected
        
    def test_calculate_date_difference_same_day(self):
        date1 = datetime(2023, 8, 15)
        date2 = datetime(2023, 8, 15)
        result = calculate_date_difference(date1, date2)
        
        assert result == 0
        
    def test_calculate_date_difference_consecutive_days(self):
        date1 = datetime(2023, 8, 15)
        date2 = datetime(2023, 8, 16)
        result = calculate_date_difference(date1, date2)
        
        assert result == 1
        
    def test_calculate_date_difference_month_apart(self):
        date1 = datetime(2023, 8, 1)
        date2 = datetime(2023, 9, 1)
        result = calculate_date_difference(date1, date2)
        
        assert result == 31
        
    def test_calculate_date_difference_year_apart(self):
        date1 = datetime(2022, 1, 1)
        date2 = datetime(2023, 1, 1)
        result = calculate_date_difference(date1, date2)
        
        assert result == 365
        
    def test_calculate_date_difference_negative(self):
        date1 = datetime(2023, 8, 15)
        date2 = datetime(2023, 8, 10)
        result = calculate_date_difference(date1, date2)
        
        assert result == -5