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
import numpy as np


def main():

    # Load and read config file
    args = io.parse_input()
    config_file_path = args.input
    #output_file_path = args.output
    config_dict = io.load_config_file(config_file_path)

    results = []

    # Validate sorting algorithms config file data
    sorting_algorithms = config_dict["sorting_algorithms"].split(",")
    sorting_algorithms = [
        sorting_algorithm.strip() for sorting_algorithm in sorting_algorithms
    ]
    sorting_algorithms = [
        sorting_algorithm.lower() for sorting_algorithm in sorting_algorithms
    ]
    valid_sorting_algorithms = [
        "selection", "bubble", "insertion", "topological", "merge", "quick"
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
    int_unsorted_lists = []
    str_unsorted_lists = []
    for unsorted_list in range(0, len(unsorted_lists)):
        try:
            int_unsorted_lists.append(
                list(np.array(unsorted_lists[unsorted_list])))
            print(type(all(int_unsorted_lists)))
        except:
            print(unsorted_lists[unsorted_list])
    truena
    """for unsorted_list in unsorted_lists:
        unsorted_list = unsorted_list.strip("[] ").split(",")
        try:
            int_unsorted_lists.append([int(element) for element in unsorted_list])
        except:
            str_unsorted_lists.append(element for element in unsorted_list)
    print(int_unsorted_lists)
    print(str_unsorted_lists)

    for unsorted_list in unsorted_lists: # Cast string elements to integer to perform a correct sorting
        unsorted_list = unsorted_list.strip("[] ").split(",")
        int_unsorted_list.append([int(element) for element in unsorted_list])
    unsorted_lists = int_unsorted_list"""

    for sorting_algorithm in sorting_algorithms:
        for unsorted_list in unsorted_lists:
            sorted_list = np.sort(sorting_algorithm, unsorted_list)
            results.append((sorting_algorithm, sorted_list))

    io.formatted_output(results)


if __name__ == "__main__":
    main()
