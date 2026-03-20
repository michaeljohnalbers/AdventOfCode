import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

DAY = X


if __name__ == "__main__":
    input_file = f"input/day{DAY}.txt"
    #input_file = f"input/day{DAY}_test.txt"

    logger.info("Starting Day %d Puzzle - %s", DAY, input_file)

    #part1(input_file)
    #part2(input_file)
