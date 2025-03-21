import logging
from app.calculator import Calculator
from app.history import History

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        # Provide a file path to the History object
        self.history = History("history.csv")  # Ensure the file path is correct


if __name__ == "__main__":
    repl = REPL()
    repl.start()

