import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

DAY = 2

def part1(inputfile : str) :
    with open(inputfile) as f:
        id_ranges : list[str] = f.readline().split(',')
        invalid_id_sum = 0
        for id_range in id_ranges:
            pieces = id_range.split('-')
            start = int(pieces[0])
            end = int(pieces[1])
            logger.debug("Working on %d - %d", start, end)
            for product_id_num in range(start, end+1):
                product_id = str(product_id_num)
                logger.debug("  looking at %s", product_id)
                product_id_len = len(product_id)
                if product_id_len % 2 == 0:
                    half = product_id_len // 2
                    if product_id[0:half] == product_id[half:]:
                        logger.info("===> Found bad id: %s", product_id)
                        invalid_id_sum += product_id_num

    logger.info("Sum of bad product IDs: %s", invalid_id_sum)

                # for sequence_size in range(1, product_id_len // 2):
                #     possible_sequence = product_id[0:sequence_size]
                #     found_sequence = True
                #     for sequence_start in range(sequence_size, product_id_len, sequence_size):
                #         if possible_sequence != product_id[sequence_start:(sequence_start + sequence_size)]:
                #             found_sequence = False
                #             break
                #     if found_sequence:
                #         logger.info("Found bad id: %s", product_id)
                #         break

def part2(inputfile : str):
    with open(inputfile) as f:
        id_ranges : list[str] = f.readline().split(',')
        invalid_id_sum = 0
        for id_range in id_ranges:
            pieces = id_range.split('-')
            start = int(pieces[0])
            end = int(pieces[1])
            logger.debug("Working on %d - %d", start, end)
            for product_id_num in range(start, end+1):
                product_id = str(product_id_num)
                logger.debug("  looking at %s", product_id)
                product_id_len = len(product_id)

                for sequence_size in range(1, (product_id_len // 2) + 1):
                    possible_sequence = product_id[0:sequence_size]
                    found_sequence = True
                    for sequence_start in range(sequence_size, product_id_len, sequence_size):
                        logger.debug("For %s, checking x[%d:%d]", product_id, sequence_start, (sequence_start + sequence_size))
                        if possible_sequence != product_id[sequence_start:(sequence_start + sequence_size)]:
                            found_sequence = False
                            break
                    if found_sequence:
                        logger.info("Found bad id: %s", product_id)
                        invalid_id_sum += product_id_num
                        break

    logger.info("Sum of bad product IDs: %s", invalid_id_sum)

if __name__ == "__main__":
    input_file = f"input/day{DAY}.txt"
    #input_file = f"input/day{DAY}_test.txt"

    logger.info("Starting Day %d Puzzle - %s", DAY, input_file)

    #part1(input_file)
    part2(input_file)
