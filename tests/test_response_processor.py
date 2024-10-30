# tests/test_response_processor.py

import pytest
from openai_integration.response_processor import ResponseProcessor
from unittest.mock import patch
import sys
from io import StringIO

@pytest.fixture
def processor():
    """Fixture to initialize ResponseProcessor."""
    return ResponseProcessor()

def test_process_response_valid_format(processor):
    """Test processing a valid commit message."""
    valid_message = "fix | Backend: Correct API endpoint response"
    result = processor.process_response(valid_message)
    assert result == valid_message

def test_process_response_invalid_format(processor):
    """Test processing an invalid commit message format."""
    invalid_message = "Fixed the API endpoint response"
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(invalid_message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_empty_response(processor):
    """Test processing an empty commit message."""
    empty_message = ""
    result = processor.process_response(empty_message)
    assert result is None

    none_message = None
    result = processor.process_response(none_message)
    assert result is None

def test_process_response_different_change_types(processor):
    """Test processing commit messages with various change types."""
    change_types = ["feature", "bugfix", "refactor", "docs", "test", "chore"]
    for change_type in change_types:
        message = f"{change_type} | UI: Improve button responsiveness"
        result = processor.process_response(message)
        assert result == message

def test_process_response_unknown_change_type(processor):
    """Test processing a commit message with an unknown change type."""
    unknown_type_message = "enhancement | UI: Add dark mode support"
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(unknown_type_message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_missing_impact_area(processor):
    """Test processing a commit message missing the impact area."""
    missing_impact_message = "fix | : Correct API response"
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(missing_impact_message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_extra_sections(processor):
    """Test processing a commit message with extra sections."""
    extra_section_message = "fix | Backend: Correct API response | urgent"
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(extra_section_message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_multiline_message(processor):
    """Test processing a multiline commit message."""
    multiline_message = """fix | Backend: Correct API response
    Added error handling for unexpected inputs."""
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(multiline_message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_valid_message_with_special_characters(processor):
    """Test processing a valid commit message containing special characters."""
    valid_message = "docs | Frontend: Update README.md with new instructions!"
    result = processor.process_response(valid_message)
    assert result == valid_message

def test_process_response_invalid_change_type_case_insensitive(processor):
    """Test that change types are case-sensitive."""
    message = "Fix | Backend: Correct API response"  # 'Fix' vs 'fix'
    
    with patch('builtins.print') as mock_print:
        result = processor.process_response(message)
        assert result is None
        mock_print.assert_called_with("Generated commit message does not match the required format.")

def test_process_response_valid_with_numeric_impact_area(processor):
    """Test processing a valid commit message with numeric impact area."""
    message = "fix | API2: Correct endpoint response"
    result = processor.process_response(message)
    assert result == message
