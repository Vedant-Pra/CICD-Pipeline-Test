import pytest
from myapp import myFunc  # Assume your program is saved in 'your_program_file.py'

def test_myFunc(monkeypatch):
    # Mock the input to return 'Alice'
    monkeypatch.setattr('builtins.input', lambda _: 'Alice')
    
    # Check if the function returns the correct greeting
    assert myFunc() == "Hello, Alice!"