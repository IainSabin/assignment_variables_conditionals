"""
Test module for main.py.
Tests for the Variables and Conditional Statements assignment.
"""

# cspell:ignore capsys

import sys
from pathlib import Path

# Add parent directory to path to import main module
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import main


def test_main_runs_without_error(capsys):
    """Test that main function runs without error."""
    main()
    captured = capsys.readouterr()
    # Should have output
    assert len(captured.out) > 0


def test_main_prints_member_name(capsys):
    """Test that main function prints the member's name."""
    main()
    captured = capsys.readouterr()
    assert "Name" in captured.out or "name" in captured.out


def test_main_prints_book_count(capsys):
    """Test that main function prints the number of books checked out."""
    main()
    captured = capsys.readouterr()
    assert "book" in captured.out.lower() or "Books" in captured.out


def test_main_prints_account_status(capsys):
    """Test that main function prints whether the account is active."""
    main()
    captured = capsys.readouterr()
    assert (
        "active" in captured.out.lower()
        or "Account" in captured.out
        or "True" in captured.out
        or "False" in captured.out
    )


def test_main_prints_checkout_message(capsys):
    """Test that main function prints a checkout eligibility message."""
    main()
    captured = capsys.readouterr()
    output_lower = captured.out.lower()
    # Check for keywords related to checkout rules
    assert any(
        keyword in output_lower
        for keyword in [
            "checkout",
            "can",
            "cannot",
            "eligible",
            "rule",
            "check",
            "books",
        ]
    )


def test_main_has_at_least_four_print_statements(capsys):
    """Test that main function has at least 4 print statements."""
    main()
    captured = capsys.readouterr()
    # Count non-empty lines (at least 4 meaningful outputs expected)
    lines = [line.strip() for line in captured.out.split("\n") if line.strip()]
    assert len(lines) >= 4


def test_main_returns_none():
    """Test that main function returns None."""
    result = main()
    assert result is None
