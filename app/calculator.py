import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Calculator:
    def evaluate(self, expression):
        try:
            result = eval(expression, {}, {})
            logging.info(f"Evaluated expression: {expression} = {result}")
            return result
        except Exception as e:
            logging.error(f"Invalid expression: {expression}")
            raise ValueError("Invalid expression")

