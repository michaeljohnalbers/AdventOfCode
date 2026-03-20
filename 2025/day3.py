import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

DAY = 3

def part1(inputfile : str) :
    with open(inputfile) as f:
        total_joltage = 0
        for bank in f.readlines():
            bank = bank.strip()
            logger.debug("Bank: %s", bank)
            first_battery = "-1"
            first_battery_position = 0
            for index, battery in enumerate(bank[0:len(bank)-1]):
                if int(battery) > int(first_battery):
                    first_battery = battery
                    first_battery_position = index
            second_battery = "-1"
            for battery in bank[first_battery_position+1:len(bank)]:
                if int(battery) > int(second_battery):
                    second_battery = battery
            bank_joltage = int(first_battery + second_battery)
            logger.debug('  joltage: %d', bank_joltage)
            total_joltage += bank_joltage

        logger.info("Total joltage: %d", total_joltage)

def part2(inputfile : str) :
    NUM_BATTERIES :int = 12
    with open(inputfile) as f:
        total_joltage = 0
        for bank in f.readlines():
            bank = bank.strip()
            logger.debug("Bank: %s (length == %d)", bank, len(bank))
            battery_string : str = ''
            battery_position = 0
            for battery_number in range(0, NUM_BATTERIES):
                battery_value = '-1'
                batteries_need_left = NUM_BATTERIES - battery_number
                end_index = len(bank) - batteries_need_left + 1
                bank_subset = bank[battery_position:end_index]
                logger.debug('  "%s" - need left: %d. Start: %d, end: %d, subset: %s',
                            battery_string.zfill(NUM_BATTERIES), batteries_need_left, battery_position, end_index,
                            bank_subset)
                saved_index = 0
                for index, current_battery in enumerate(bank_subset):
                    if int(current_battery) > int(battery_value):
                        battery_value = current_battery
                        saved_index = index
                battery_position = battery_position + saved_index + 1
                battery_string += battery_value
            logger.debug("  - joltage %s", battery_string)
            total_joltage += int(battery_string)

        logger.info("Total joltage: %d", total_joltage)


if __name__ == "__main__":
    input_file = f"input/day{DAY}.txt"
    #input_file = f"input/day{DAY}_test.txt"

    logger.info("Starting Day %d Puzzle - %s", DAY, input_file)

    part1(input_file)
    part2(input_file)
