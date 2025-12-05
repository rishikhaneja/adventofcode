import os

from importlib import import_module

solution_dir = os.path.dirname(os.path.abspath(__file__))
year_dir = os.path.dirname(solution_dir)
input_dir = os.path.join(year_dir, "input")
output_dir = os.path.join(year_dir, "output")
os.makedirs(output_dir, exist_ok=True)

for day in range(1, 12):

    input_path = os.path.join(input_dir, f"{day}.txt")
    output_path = os.path.join(output_dir, f"{day}.txt")

    try:
        solution_module = import_module(f"{day}")
    except ModuleNotFoundError:
        print("Stopping here. No more solutions found.")
        exit(0)

    print(f"Day {day}:")
    result = solution_module.solve(input_path)
    
    with open(output_path, 'w') as output_file:
        output_file.write(result)


        