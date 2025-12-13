import logging
from io import TextIOWrapper

logger = logging.getLogger(__name__)

def solve(input_file: TextIOWrapper):
    total = 0
    for line in input_file:
        line = line.strip()
        largest_left, position_left = largest_first(line[:-1])
        largest_right, _ = largest_first(line[position_left + 1:])
        largest = largest_left + largest_right
        total += int(largest)
        logger.info(f"In line '{line}', largest joltage possible is {largest}")
    logger.info(f"Total possible joltage is {total}")

def largest_first(digits: str) -> tuple[str, int]:
    largest = '0'
    position = 0
    for i, digit in enumerate(digits):
        if digit > largest:
            largest = digit
            position = i
    return largest, position