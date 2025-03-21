import os
import pytest
from app.history import History

@pytest.fixture
def history():
    file_path = "history.csv"
    history = History(file_path)
    return history

def test_get_history(history):
    # Add an initial entry, which is automatically in history when the file is created
    history.add_entry("2 + 2", 4)  # Assuming this entry is already in the file when it's created
    history.add_entry("5 + 5", 10)  # Now we add a new entry

    # Get the current history and verify the length
    history_data = history.get_history()

    # Assert that there are 2 entries in the history now (existing + newly added)
    assert len(history_data) == 2

