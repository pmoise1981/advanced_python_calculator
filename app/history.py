import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class History:
    def __init__(self, file_path="data/history.csv"):
        self.file_path = file_path
        if not os.path.exists(file_path):
            pd.DataFrame(columns=["Expression", "Result"]).to_csv(file_path, index=False)

    def add_entry(self, expression, result):
        df = pd.read_csv(self.file_path)
        new_entry = pd.DataFrame({"Expression": [expression], "Result": [result]})
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(self.file_path, index=False)
        logging.info(f"Added history entry: {expression} = {result}")

    def get_history(self):
        return pd.read_csv(self.file_path)

