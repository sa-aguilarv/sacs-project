""" Sort algorithms module
This module contains all the sort algorithms seen during the ToC course
Functions:
    Quick sort: Sort an array of number, letters, and objects using the 
    quick sort strategy.
    Bubble sort: Sort an array of number, letters, and objects using the
    bubble sort strategy
"""

import time


def sort(sorting_algorithm: str, unsorted_list: list) -> dict:
    """_summary_

    Args:
        sorting_algorithm (str): _description_
        unsorted_list (list): _description_

    Returns:
        list: _description_
    """
    output_dict = None
    if sorting_algorithm == "quick":
        output_dict = quick_sort(unsorted_list)
    elif sorting_algorithm == "bubble":
        output_dict = bubble_sort(unsorted_list)
    elif sorting_algorithm == "selection":
        output_dict = selection_sort(unsorted_list)
    elif sorting_algorithm == "insertion":
        output_dict = insertion_sort(unsorted_list)
    elif sorting_algorithm == "merge":
        start_time = time.perf_counter()
        merge_sort(unsorted_list)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        output_dict = {
            "sorted_list": unsorted_list,
            "elapsed_time": elapsed_time
        }
    return output_dict


def quick_sort(unsorted_list: list) -> dict:
    """Sort a list of numbers, letters, and objects using the brute force
    strategy called Quick sort
    This method identify the list's values types and sort them.
    Parameters
    ----------
    unsorted_list: list
        A is list with the elements to be sorted
    Returns
    ---------
    list
        a list of sorted values or objects
        
    """

    sorted_list = unsorted_list.copy()
    sorted_list_length = len(sorted_list)

    start_time = time.perf_counter()
    for i in range(sorted_list_length - 1):
        minimum = i
        for j in range(i + 1, sorted_list_length):
            if sorted_list[j] > sorted_list[minimum]:
                minimum = j
        swap_values(i, minimum, sorted_list)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    output_dict = {"sorted_list": sorted_list, "elapsed_time": elapsed_time}
    return output_dict


def bubble_sort(unsorted_list: list) -> dict:
    """ Sort a list of numbers, letters, and objects using the brute 
    force strategy called Bubble sort.
    This method identify the list's values type and sort them.
    Parameters
    ---------------
    unsorted_list : list
        unsorted_list is a list with the elements to be sorted
    Returns
    ---------------
    list
        a list of sorted values or objects
    """

    sorted_list = unsorted_list.copy()
    list_length = len(unsorted_list)

    start_time = time.perf_counter()
    for i in range(list_length - 1):
        for j in range(list_length - 1 - i):
            if sorted_list[j + 1] > sorted_list[j]:
                swap_values(j, j + 1, sorted_list)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    output_dict = {"sorted_list": sorted_list, "elapsed_time": elapsed_time}
    return output_dict


def selection_sort(unsorted_list: list) -> dict:
    """_summary_

    Args:
        unsorted_list (list): _description_

    Returns:
        dict: _description_
    """
    sorted_list = unsorted_list.copy()
    list_length = len(unsorted_list)
    # Traverse through all array elements
    start_time = time.perf_counter()
    for i in range(list_length):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, list_length):
            if sorted_list[min_idx] < sorted_list[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        sorted_list[i], sorted_list[min_idx] = sorted_list[
            min_idx], sorted_list[i]
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    output_dict = {"sorted_list": sorted_list, "elapsed_time": elapsed_time}
    return output_dict


def insertion_sort(unsorted_list: list) -> dict:
    """_summary_

    Args:
        unsorted_list (list): _description_

    Returns:
        dict: _description_
    """
    sorted_list = unsorted_list.copy()
    list_length = len(unsorted_list)
    # Traverse through all array elements
    start_time = time.perf_counter()
    # Traverse through 1 to len(arr)
    for i in range(1, list_length):
        key = sorted_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key > sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    output_dict = {"sorted_list": sorted_list, "elapsed_time": elapsed_time}
    return output_dict


def merge_sort(myList):
    """_summary_

    Args:
        myList (_type_): _description_
    """
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


def swap_values(i: int, j: int, list_to_swap: list):
    """ Swap the values of the index i and j in the list_to_swap list
        Parameters
        ------------
        i: int
            index of the first value to swap
        j: int
            index of the second value to swap
        list_to_swap: list
            list where the swap will be performed
    """

    temp = list_to_swap[i]
    list_to_swap[i] = list_to_swap[j]
    list_to_swap[j] = temp
