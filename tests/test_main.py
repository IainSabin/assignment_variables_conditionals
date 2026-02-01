"""
Test module for main.py.
This demonstrates basic pytest usage.
"""

import sys
from pathlib import Path

# Add parent directory to path to import main module
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import main


def test_main_runs_without_error(capsys):
    """Test that main function runs without error and prints expected output."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out


def test_main_returns_none():
    """Test that main function returns None."""
    result = main()
    assert result is None
