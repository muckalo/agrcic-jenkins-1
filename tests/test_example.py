# test_example.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the parent directory to the path
import pytest
from example import add


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


if __name__ == '__main__':
    pytest.main()
