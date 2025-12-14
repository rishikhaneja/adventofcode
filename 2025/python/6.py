import logging
import math
from io import TextIOWrapper

logger = logging.getLogger(__name__)

def solve(input_file: TextIOWrapper):
    answer = 0
    grid = [line.split() for line in input_file]
    row_count = len(grid)
    assert row_count == 5, f"Expected 5 rows, got {row_count}"
    col_count = len(grid[0])
    for col in range(col_count):
        operation = grid[4][col]
        values = [int(grid[row][col]) for row in range(4)]
        answer += (sum(values) if operation == '+' else math.prod(values))
    logger.info(f"Answer: {answer}")