import argparse
import re

# Check compilation bugs (commas)
SORTING_ALGORITHMS_PATTERN = "(sorting_algorithms)\s?=(\s?([A-Za-z]+)(,\s?[A-Za-z]+)+)"
UNSORTED_LIST_PATTERN = ""


def parsing_input() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    # Define INPUT argument
    parser.add_argument("-i", "--input", help="Input file for SACS", required=True)
    parser.add_argument("-o", "--output", help="Output file for SACS")
    # Store NAMESPACE object
    args = parser.parse_args()
    print(args.input)
    return args


def load_config_file(file_path: str) -> dict:
    f = open(file_path, "r")
    # Read data in file as a whole str
    text = f.read()
    f.close()

    re_obj = re.compile(SORTING_ALGORITHMS_PATTERN)
    # Build automata to compile str pattern
    match_obj = re_obj.search(text)

    # Access pattern stored values based on index
    print(match_obj.group(2))


def output_table(comparison_structure: dict):
    pass
