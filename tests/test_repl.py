
import pytest
from unittest.mock import patch
from app.repl import REPL

def test_repl_addition():
    with patch("builtins.input", side_effect=["2 + 2", "exit"]):
        repl = REPL()
        repl.start()
        # Assuming we mock the input to simulate entering the calculation
        assert repl.calculator.evaluate("2 + 2") == 4

def test_repl_history():
    with patch("builtins.input", side_effect=["2 + 2", "history", "exit"]):
        repl = REPL()
        repl.start()
        history = repl.history.get_history()
        assert len(history) > 0
        assert history.iloc[-1]["Expression"] == "2 + 2"

