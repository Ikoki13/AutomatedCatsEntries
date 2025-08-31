import logging
import os
import sys
from datetime import timedelta
from unittest.mock import Mock

# Add the src directory to the Python path BEFORE any src imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from src.Classes.CATsCell import CATsCell

@pytest.fixture
def empty_cell():
    return CATsCell()

@pytest.fixture
def mock_time_entry():
    mock = Mock()
    mock.duration = 3600  # 1 hour in seconds
    mock.getCatFormat.return_value = "Test entry"
    return mock

def test_cell_initialization(empty_cell):
    assert empty_cell.cellText == ''
    assert empty_cell.duration == 0.0
    assert empty_cell.maximumNumberOfCharacters == 220

def test_str_representation(empty_cell):
    empty_cell.cellText = "Test entry"
    empty_cell.duration = 1.0
    expected = "Duration:\n1.0\nText:\nTest entry"
    assert str(empty_cell) == expected

def test_str_representation_rounds_duration(empty_cell):
    empty_cell.cellText = "Test entry"
    empty_cell.duration = 1.333333
    expected = "Duration:\n1.25\nText:\nTest entry"
    assert str(empty_cell) == expected

def test_add_time_entry_success(empty_cell, mock_time_entry):
    result = empty_cell.addTimeEntry(mock_time_entry)
    assert result is True
    assert empty_cell.cellText == "Test entry\n"
    assert empty_cell.duration == 1.0

def test_add_time_entry_too_long(empty_cell, mock_time_entry):
    # Create entry longer than maximum characters
    mock_time_entry.getCatFormat.return_value = "x" * 221
    result = empty_cell.addTimeEntry(mock_time_entry)
    assert result is False
    assert empty_cell.cellText == ""
    assert empty_cell.duration == 0.0

def test_add_multiple_time_entries(empty_cell, mock_time_entry):
    # First entry
    result1 = empty_cell.addTimeEntry(mock_time_entry)
    
    # Second entry
    mock_time_entry2 = Mock()
    mock_time_entry2.duration = 1800  # 30 minutes in seconds
    mock_time_entry2.getCatFormat.return_value = "Second entry"
    result2 = empty_cell.addTimeEntry(mock_time_entry2)

    assert result1 is True
    assert result2 is True
    assert empty_cell.cellText == "Test entry\nSecond entry\n"
    assert empty_cell.duration == 1.5  # 1 hour + 30 minutes

def test_add_time_entry_cell_full(empty_cell, mock_time_entry):
    # Fill the cell close to maximum
    mock_time_entry.getCatFormat.return_value = "x" * 210
    first_result = empty_cell.addTimeEntry(mock_time_entry)
    
    # Try to add another entry
    mock_time_entry2 = Mock()
    mock_time_entry2.duration = 3600
    mock_time_entry2.getCatFormat.return_value = "One more entry"
    second_result = empty_cell.addTimeEntry(mock_time_entry2)

    assert first_result is True
    assert second_result is False
    assert empty_cell.duration == 1.0  # Only first entry counted
