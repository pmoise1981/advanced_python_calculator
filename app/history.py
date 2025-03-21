import pandas as pd
import os
import logging


class History:
    def __init__(self, file_path):
        self.file_path = file_path
        # Ensure the file exists and has the necessary header
        self.setup_history_file()

    def setup_history_file(self):
        """Ensure the history file exists and has a header."""
        if not os.path.exists(self.file_path):
            # If the file does not exist, create it with an empty DataFrame
            df = pd.DataFrame(columns=["expression", "result"])
            df.to_csv(self.file_path, index=False)

    def add_entry(self, expression, result):
        try:
            df = pd.read_csv(self.file_path)
        except pd.errors.EmptyDataError:
            # Create an empty DataFrame if the file is empty
            df = pd.DataFrame(columns=["expression", "result"])

        # Add the new entry
        new_entry = pd.DataFrame({"expression": [expression], "result": [result]})
        df = pd.concat([df, new_entry], ignore_index=True)

        # Save the updated file
        df.to_csv(self.file_path, index=False)

    def get_history(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except pd.errors.EmptyDataError:
            # If the file is empty, return an empty DataFrame
            return pd.DataFrame(columns=["expression", "result"])

