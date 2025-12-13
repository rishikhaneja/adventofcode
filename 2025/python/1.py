import logging
import sys

logger = logging.getLogger(__name__)

def solve(input_file):
    logger.info("The dial starts by pointing at 50.")
    current = 50
    password = 0
    for line in input_file:
        line = line.strip()
        direction, value = line[0], int(line[1:])
        current = (current + value * (1 if direction == 'R' else -1)) % 100
        hit = current == 0
        password += 1 if hit else 0
        logger.info(f"The dial is rotated {direction}{value} to point at {current}. {'*' if hit else ''}")
    logger.info(f"Because the dial points at 0 a total of {password} times during this process, the password in this example is {password}.")