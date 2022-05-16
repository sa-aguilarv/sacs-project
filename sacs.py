#! /usr/bin/env python
"""Access point to the Sorting Algorithm Comparison System (SACS)
    The SACS performs an elapsed time comparison between different sorting algorithms from different strategies.
    ------------
    Functions
    ------------
    main:
        Access point to the SACS system. It controls the program's workflow.
"""

import sorting_algorithms as sa
import sorting_algorithms_desc as sad
import input_output as io
import re

PATTERN_STR_LIST = "[a-zA-Z]"


def main():
    """Access point to the SACS system. It controls the program's workflow.
    ------------
    Raises
    ------------
    SystemExit: 
        ValueError if invalid sorting algorithm was entered. Valid sorting algorithms are "selection", "bubble", "insertion", "merge", "quick".
    SystemExit: 
        ValueError because each list's items must be of the same data type.
    SystemExit:
        ValueError if selected sorting order is invalid. Valid sorting orders are "asc" or "desc".
    """
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
        print("\nValueError: invalid sorting algorithm was entered: " +
              str(invalid_sorting_algorithms))
        print("Valid sorting algorithms are: " + str(valid_sorting_algorithms))
        raise SystemExit(0)
    if len(invalid_sorting_algorithms) == 0:
        validated_sorting_algorithms = sorting_algorithms
        print("\nSelected sorting algorithms are: " +
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
    for unsorted_list in int_unsorted_lists:
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
                "\nValueError: each list's items must be of the same data type."
            )
            print("Invalid input: " + str(unsorted_list))
            raise SystemExit(0)

    print("\nEntered lists are:")
    print(validated_int_unsorted_lists)
    print(validated_str_unsorted_lists)

    # Validate sorting order config file data
    sorting_order = config_dict["order"]

    # Start sorting comparison
    validated_unsorted_lists = validated_int_unsorted_lists + validated_str_unsorted_lists
    results = []
    if sorting_order == "asc":
        print("\nSelected sorting order is: " + sorting_order + "\n")
        for sorting_algorithm in validated_sorting_algorithms:
            for unsorted_list in validated_unsorted_lists:
                output_dict = sa.sort(sorting_algorithm, unsorted_list)
                results.append((sorting_algorithm, output_dict))
    elif sorting_order == "desc":
        print("\nSelected sorting order is: " + sorting_order + "\n")
        for sorting_algorithm in validated_sorting_algorithms:
            for unsorted_list in validated_unsorted_lists:
                output_dict = sad.sort(sorting_algorithm, unsorted_list)
                results.append((sorting_algorithm, output_dict))
    else:
        print("\nValueError: selected sorting order is invalid: " +
              sorting_order)
        print("Valid inputs are: asc or desc")
        raise SystemExit(0)

    # Print output
    io.formatted_output(results)

    # Calculate average sorting time per sorting algorithm
    def average(lst):
        return sum(lst) / len(lst)

    avg_elapsed_time_list = []
    for sorting_algorithm in validated_sorting_algorithms:
        avg_elapsed_time = 0
        elapsed_time_list = []
        for item in results:
            aux_sorting_algorithm = item[0]
            if sorting_algorithm == aux_sorting_algorithm:
                elapsed_time = item[1]["elapsed_time"]
                elapsed_time_list.append(elapsed_time)
        avg_elapsed_time = average(elapsed_time_list)
        print("\n- " + sorting_algorithm + " sort average elapsed time: " +
              str(avg_elapsed_time))
        avg_elapsed_time_list.append((sorting_algorithm, avg_elapsed_time))

    # Calculate min avg sorting time per sorting algorithm
    names = []
    times = []
    for item in avg_elapsed_time_list:
        names.append(item[0])
        times.append(item[1])
    max_value = min(times)
    index_max_value = times.index(max_value)
    print("\nThe fastest sorting algorithm is " + str(names[index_max_value]) +
          " sort with average elapsed time of " + str(max_value))


if __name__ == "__main__":
    main()
