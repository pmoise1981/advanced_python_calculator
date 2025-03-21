import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def square(number):
    result = number ** 2
    logging.info(f"Square of {number}: {result}")
    return result

