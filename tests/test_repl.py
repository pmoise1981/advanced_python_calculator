
import pytest
from unittest.mock import patch
from app.repl import REPL

def test_repl_addition():
    with patch("builtins.input", side_effect=["2 + 2", "exit"]):
        repl = REPL()
        # Rest of the test logic


