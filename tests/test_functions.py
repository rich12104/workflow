import sys
import os

<<<<<<< HEAD
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import main  # Import your main.py functions

def test_greet():
    assert main.greet() == "Hello, GitHub Actions!"
=======
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../workflow")))

import main    # Import your main.py functions

def test_greet():
    assert main.greet() == "Hello, GitHub Actions!"
>>>>>>> 6ecd3aca41ba9afab709281a05ee0bdaf509a01e
