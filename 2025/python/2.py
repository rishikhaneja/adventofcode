from io import TextIOWrapper
import logging

logger = logging.getLogger(__name__)
def solve(input_file: TextIOWrapper):
    sum_invalid = 0
    for range_str in input_file.read().split(","):
        range_start, range_end = range_str.split("-")
        logger.info(f"Checking IDs in range {range_start}-{range_end}:")
        for id_num in range(int(range_start), int(range_end) + 1):
            id_str = str(id_num)
            half = len(id_str) // 2
            if id_str[:half] == id_str[half:]:
                sum_invalid += id_num
                logger.info(f"ID {id_num} is invalid.")
    logger.info(f"The sum of all invalid IDs is {sum_invalid}.")