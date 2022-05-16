#! /usr/bin/env python
"""Access point to the Sorting Algorithm Comparison System (SACS)
    The SACS performs a elapse time comparison between different Sorting algorithms from different strategies.
    Functions
    ------------
    main:
        Access point to the SACS system. It controls all the program flow.
"""

from email.headerregistry import AddressHeader
from logging import exception
from queue import Empty
from warnings import catch_warnings
import sorting_algorithms as sa
import input_output as io
import re

PATTERN_STR_LIST = "[a-zA-Z]"


def main():

    # Load and read config file
    args = io.parse_input()
    config_file_path = args.input
    #output_file_path = args.output
    config_dict = io.load_config_file(config_file_path)

    # Validate sorting algorithms config file data
    sorting_algorithms = config_dict["sorting_algorithms"].split(",")
    sorting_algorithms = [
        sorting_algorithm.strip() for sorting_algorithm in sorting_algorithms
    ]
    sorting_algorithms = [
        sorting_algorithm.lower() for sorting_algorithm in sorting_algorithms
    ]
    valid_sorting_algorithms = [
        "selection", "bubble", "insertion", "merge", "quick"
    ]
    invalid_sorting_algorithms = [
        sorting_algorithm for sorting_algorithm in sorting_algorithms
        if sorting_algorithm not in valid_sorting_algorithms
    ]
    if len(invalid_sorting_algorithms) != 0:
        print("ValueError: invalid sorting algorithm was entered: " +
              str(invalid_sorting_algorithms))
        print("Valid sorting algorithms are: " + str(valid_sorting_algorithms))
        raise SystemExit(0)
    if len(invalid_sorting_algorithms) == 0:
        validated_sorting_algorithms = sorting_algorithms
        print("Selected sorting algorithms are: " +
              str(validated_sorting_algorithms))

    # Validate unsorted lists config file data
    unsorted_lists = config_dict["unsorted_lists"].split("|")
    str_obj = re.compile(PATTERN_STR_LIST)

    str_unsorted_lists = []
    int_unsorted_lists = []
    for item in range(0, len(unsorted_lists)):
        result = str_obj.search(unsorted_lists[item])
        if result is None:
            int_unsorted_lists.append(unsorted_lists[item])
        else:
            str_unsorted_lists.append(unsorted_lists[item])

    validated_int_unsorted_lists = []
    for unsorted_list in int_unsorted_lists:  # Cast string elements to integer to perform a correct sorting
        unsorted_list = unsorted_list.strip("[] ").split(",")
        validated_int_unsorted_lists.append(
            [int(element) for element in unsorted_list])

    validated_str_unsorted_lists = []
    for unsorted_list in str_unsorted_lists:
        unsorted_list = unsorted_list.strip("[] ").split(",")
        result = [re.findall("\d+", item) for item in unsorted_list]
        if not any(result):
            validated_str_unsorted_lists.append(unsorted_list)
        else:
            print(
                "ValueError: each list's items must be of the same data type.")
            print("Invalid input: " + str(unsorted_list))
            raise SystemExit(0)

    print("Entered lists are:")
    print(validated_int_unsorted_lists)
    print(validated_str_unsorted_lists)

    # Validate sorting order config file data
    sorting_order = config_dict["order"]
    print("Selected sorting order is: " + sorting_order)

    # Start sorting comparison
    validated_unsorted_lists = validated_int_unsorted_lists + validated_str_unsorted_lists
    results = []
    for sorting_algorithm in validated_sorting_algorithms:
        for unsorted_list in validated_unsorted_lists:
            sorted_list = sa.sort(sorting_algorithm, unsorted_list)
            results.append((sorting_algorithm, sorted_list))

    io.formatted_output(results)


if __name__ == "__main__":
    main()
