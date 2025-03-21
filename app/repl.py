import logging
from app.calculator import Calculator
from app.history import History

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history = History()

    def start(self):
        print("Welcome to the Advanced Calculator! Type 'exit' to quit.")
        while True:
            command = input(">> ")
            if command.lower() == "exit":
                print("Goodbye!")
                break
            elif command.lower() == "history":
                print(self.history.get_history())
            else:
                try:
                    result = self.calculator.evaluate(command)
                    self.history.add_entry(command, result)
                    print("Result:", result)
                except Exception as e:
                    logging.error(f"Error: {e}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()

