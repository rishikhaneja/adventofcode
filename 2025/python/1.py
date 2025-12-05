import sys

def solve(input_path):

    with open(input_path, 'r') as input_file:
        data = input_file.read()

    print("The dial starts by pointing at 50.")
    current = 50

    result = 0

    for line in data.splitlines():

        line = line.strip()

        direction = line[0]
        value = int(line[1:])
        if direction == 'R':
            current = ((current + value) % 100)
        elif direction == 'L':
            current = ((current - value) % 100)

        print(f"The dial is rotated {direction}{value} to point at {current}. {'*' if current == 0 else ''}")

        if current == 0:
            result += 1

    print(f"Because the dial points at 0 a total of {result} times during this process, the password in this example is {result}.")

    return str(result)