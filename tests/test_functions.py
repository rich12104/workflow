import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import main  # Import your main.py functions

def test_greet():
    assert main.greet() == "Hello, GitHub Actions!"