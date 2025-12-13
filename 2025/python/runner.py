import os
import logging
from importlib import import_module

logging.basicConfig(
    level=logging.INFO,
    format='%(module)s: %(message)s',
    handlers=[
        logging.FileHandler("runner.log", mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

input_dir = os.path.join(os.path.dirname(__file__), "..", "input")
for day in range(1, 12):
    try:
        solution_module = import_module(f"{day}")
    except ModuleNotFoundError:
        break
    logger.info(f"Day {day}:")
    with open(os.path.join(input_dir, f"{day}.txt"), 'r') as input_file:
        solution_module.solve(input_file)