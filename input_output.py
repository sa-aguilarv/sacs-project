"""The input_output module contains several functions to load files and to format the SACS outputs.
    ------------
    Functions
    ---------------
    load_config_file(file_path:str)->dict
"""

import argparse
import re

PATTERN_SORTING_ALGORITHMS = "(sorting_algorithms)\s*=\s*([a-zA-Z]+(,\s?[a-zA-Z]*)*)"
PATTERN_UNSORTED_LIST = "(unsorted_lists)\s*=\s*((\[(\w,?)+\])(\|\[(\w,?)+\])*)"
PATTERN_ORDER = "(order)\s*=\s*([a-zA-Z]+)"
PATTERNS_CONFIG_FILE = [
    PATTERN_SORTING_ALGORITHMS, PATTERN_UNSORTED_LIST, PATTERN_ORDER
]


def load_config_file(file_path: str) -> dict:
    """Load config file
    Read the config file and create a dictionary with the configuration information for used in SACS

    Args:
        file_path (str): File path and name of the configuration file

    Returns:
        dict: Dictionary with the information stored in the configuration file.
    """
    config_dict = {}

    # Open and read file
    f = open(file_path, 'r')
    text = f.read()
    f.close()

    for pattern in PATTERNS_CONFIG_FILE:
        re_obj = re.compile(pattern)
        result = re_obj.search(text)
        config_dict[result.group(1)] = result.group(2)

    return config_dict


def formatted_output(results: list):
    """Write a formated table with the results of the comparison
    The table contains a header with the information. Every row represents the evaluation of one sorting algorithm on a list of elements

    Args:
        results (list): The results obtained from the differents comparisons. The results argument is list of Tuples, every Tuple contains: (algorith_name, physical_address, sorted_list, elapsed_time)
    """
    header = "{0:^10}|{1:^20}|{2:^30}|{3:^30}"
    row = "{algorithm:^10}|{address:^20X}|{lista!s:^30}|{time:^30}"
    print(
        header.format("Algorithm", "Physical address", "List",
                      "Execution time"))
    for value in results:
        algorithm = value[0]
        sorted_list = value[1]
        print(
            row.format(algorithm=algorithm,
                       address=id(sorted_list),
                       lista=sorted_list["sorted_list"],
                       time=sorted_list["elapsed_time"]))


def parse_input() -> argparse.Namespace:
    """Reads the arguments of sacs

    Returns:
        argparse.Namespace: The object argparse.Namespace where the command line arguments are stored
    """
    parser = argparse.ArgumentParser(
        description='Time comparison of several sorting algorithms')
    parser.add_argument('-i',
                        '--input',
                        help='Config file path',
                        required=True)
    parser.add_argument(
        '-o',
        '--output',
        help='Path and file name were the results are written. '
        'If not indicated, the results are written in the standard output')

    return parser.parse_args()