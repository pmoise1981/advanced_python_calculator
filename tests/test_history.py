import pytest
import os
import pandas as pd
from app.history import History

@pytest.fixture
def history():
    return History()

def test_add_history(history):
    history.add_entry("2 + 2", 4)
    df = pd.read_csv(history.file_path)
    assert len(df) > 0
    assert df.iloc[-1]["Expression"] == "2 + 2"
    assert df.iloc[-1]["Result"] == 4

def test_get_history(history):
    history.add_entry("5 + 5", 10)
    history.add_entry("10 + 10", 20)
    df = history.get_history()
    assert len(df) > 0
    assert df.iloc[-1]["Expression"] == "10 + 10"
    assert df.iloc[-1]["Result"] == 20

def test_history_file_creation(history):
    assert os.path.exists(history.file_path)

