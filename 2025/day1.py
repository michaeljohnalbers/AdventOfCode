
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z")

def do_rotations(inputfile: str, calculate_at_zero : bool) -> int:
    MAX_POSITIONS : int = 100
    with open(inputfile) as f:
        lines = f.readlines()
        position : int = 50
        ended_at_zero_count : int = 0
        encountered_zero_count : int = 0
        for rotation in lines:
            rotation = rotation.strip()
            if rotation[0] == '#':
                continue
            rotation_direction : str = rotation[0]
            rotation_amount : int = int(rotation[1:])

            full_rotations : int = rotation_amount // MAX_POSITIONS
            extra_rotation = rotation_amount - (full_rotations * MAX_POSITIONS)
            encountered_zero_count += full_rotations

            start_position : int = position
            encountered_zero : bool = False
            if rotation_direction == "L":
                p = (position - extra_rotation) % MAX_POSITIONS
                if start_position != 0 and (p > start_position or p == 0):
                    encountered_zero = True
                    encountered_zero_count += 1
                position = (position - rotation_amount) % MAX_POSITIONS
            elif rotation_direction == "R":
                p = (position + extra_rotation) % MAX_POSITIONS
                if start_position != 0 and (p < start_position):
                    encountered_zero = True
                    encountered_zero_count += 1
                position = (position + rotation_amount) % MAX_POSITIONS
            else:
                raise Exception("Invalid direction: %s", rotation_direction)

            if position == 0:
                ended_at_zero_count += 1

            encountered_string = ''
            if encountered_zero:
                encountered_string = f'({encountered_zero})'
            logger.debug(f"From %d with %s = %d, p={p} %s",
                         start_position, rotation, position, encountered_string)

    calculation_count : int
    if calculate_at_zero:
        calculation_count = ended_at_zero_count
    else:
        calculation_count = encountered_zero_count

    return calculation_count


def part1(inputFile: str):
    logger.info("=== Part 1, find the password (at zero)")
    times_at_zero = do_rotations(inputFile, True)
    logger.info("Number of times at zero: %d\n", times_at_zero)


def part2(input_file: str):
    logger.info("=== Part 2, find the password (at or crossing zero)")
    times_at_or_crossing_zero = do_rotations(input_file, False)
    logger.info("Number of times at or crossing zero: %d\n", times_at_or_crossing_zero)


if __name__ == "__main__":
    input_file = "input/day1.txt"
    #input_file = "input/day1_test.txt"

    logger.info("Starting Day 1 Puzzle - %s", input_file)

    part1(input_file)
    part2(input_file)
