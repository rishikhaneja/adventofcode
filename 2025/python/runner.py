import os
from importlib import import_module

input_dir = os.path.join(os.path.dirname(__file__), "..", "input")
for day in range(1, 12):
    try:
        solution_module = import_module(f"{day}")
    except ModuleNotFoundError:
        break
    print(f"\nDay {day}:")
    with open(os.path.join(input_dir, f"{day}.txt"), 'r') as input_file:
        solution_module.solve(input_file)