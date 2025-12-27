import logging
from io import TextIOWrapper

logger = logging.getLogger(__name__)

def solve(input_file: TextIOWrapper):
    answer = 0
    lines = [line for line in input_file]
    beams = {lines[0].index('S')}
    for line in range(1, len(lines)):
        new_beams = set()
        for beam in beams:
            if lines[line][beam] == '^':
                answer += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            elif lines[line][beam] == '.':
                new_beams.add(beam)
        beams = new_beams
    logger.info(f"Number of splits: {answer}")