import logging
from io import TextIOWrapper

logger = logging.getLogger(__name__)

def solve(input_file: TextIOWrapper):
    fresh_count = 0
    parsing_ranges = True
    ranges = []
    for line in input_file:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue
        if parsing_ranges:
            start_str, end_str = line.split('-')
            start, end = int(start_str), int(end_str)
            ranges.append((start, end))
        else:
            number = int(line)
            if any(start <= number <= end for start, end in ranges):
                fresh_count += 1
    logger.info(f"Total fresh count: {fresh_count}")