import logging
from io import TextIOWrapper

logger = logging.getLogger(__name__)

def solve(input_file: TextIOWrapper):
    count = 0
    output = []
    grid = [list(line.strip()) for line in input_file]
    row_count = len(grid)
    col_count = len(grid[0])
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] != '@':
                output.append('.')
                continue
            adjacent_count = 0
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < row_count and 0 <= nc < col_count and grid[nr][nc] == '@':
                    adjacent_count += 1
            if adjacent_count < 4:
                count += 1
                output.append('x')
            else:
                output.append('@')
        output.append('\n')
    logger.info(f"\n{''.join(output)}")
    logger.info(f"Count of '@' with less than 4 adjacent '@': {count}")