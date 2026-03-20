import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")
logger = logging.getLogger(__name__)

DAY = 4

type Table = list[list[str]]

def read_input(inputfile: str) -> Table:
    diagram: Table = []
    with open(inputfile) as f:
        diagram = [list(line.strip()) for line in f]

    return diagram

def count_column(row : list[str], column : int, current_roll : bool = False) -> int:
    count : int = 0
    if column > 0 and row[column-1] == '@':
        count += 1

    if (not current_roll) and row[column] == '@':
        count += 1

    if column < len(row) - 1 and row[column+1] == '@':
        count += 1

    return count

def count_adjacent_rolls(diagram : Table, row: int, column : int) -> int:
    if row >= len(diagram):
        raise IndexError(f"row {row} is greater than {len(diagram)}.")
    if column >= len(diagram[0]):
        raise IndexError(f"column {column} is greater than {len(diagram[0])}.")

    adjacent_rolls = 0

    if row > 0:
        adjacent_rolls += count_column(diagram[row-1], column)

    adjacent_rolls += count_column(diagram[row], column, True)

    if row < len(diagram) - 1:
        adjacent_rolls += count_column(diagram[row+1], column)

    logger.debug("For [%d,%d], adjacent count is %d.", row, column, adjacent_rolls)

    return adjacent_rolls

def part1(inputfile: str):
    diagram = read_input(inputfile)
    can_be_moved : int = 0

    for row in range(0, len(diagram)):
        for column in range(0, len(diagram[row])):
            if diagram[row][column] == '@':
                adjacent_rolls = count_adjacent_rolls(diagram, row, column)
                if adjacent_rolls < 4:
                    logger.debug('  -> Can be moved')
                    can_be_moved += 1

    logger.info("Part 1 - Rolls which can be moved: %d", can_be_moved)

def part2(inputfile: str):
    diagram = read_input(inputfile)
    can_be_moved : int = 0

    rolls_were_removed : bool = True
    round_count = 0

    while rolls_were_removed:
        round_count += 1
        rolls_were_removed = False

        removed : list[tuple[int, int]] = []

        for row_index, row in enumerate(diagram):
            for column_index, cell in enumerate(row):
                if cell == '@':
                    adjacent_rolls = count_adjacent_rolls(diagram, row_index, column_index)
                    if adjacent_rolls < 4:
                        logger.debug('  -> Can be moved')
                        can_be_moved += 1
                        rolls_were_removed = True
                        removed.append((row_index, column_index))
        logger.debug("After round %d, removed %d rolls, %d total.", round_count, len(removed), can_be_moved)

        for row, column in removed:
            diagram[row][column] = 'X'

    logger.info("Part 2 - Can remove %d rolls (after %d rounds).", can_be_moved, round_count)

if __name__ == "__main__":
    input_file = f"input/day{DAY}.txt"
    #input_file = f"input/day{DAY}_test.txt"

    logger.info("Starting Day %d Puzzle - %s", DAY, input_file)

    part1(input_file)
    part2(input_file)
