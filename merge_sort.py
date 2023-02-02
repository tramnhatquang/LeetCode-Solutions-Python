from typing import *


def mergesort_algo_monster(arr):
    # base case
    if len(arr) < 2:
        return arr
    # the divide step: split array into two components, assuming they are sorted recursively
    mid = len(arr) // 2
    left = mergesort_algo_monster(arr[:mid])
    right = mergesort_algo_monster(arr[mid:])
    # the merging (conquer) step: combine two components to get the final result
    l, r, result = 0, 0, []
    while l < len(left) or r < len(right):
        if l >= len(left) or (r < len(right) and left[l] > right[r]):
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1
    return result


def mergeSort_educative(myList: List[int]) -> List[int]:
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort_educative(left)
        mergeSort_educative(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
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

    return myList
    # time = O(n log n), n is length of arr
    # space: O(n)


if __name__ == '__main__':
    unsorted_arr_1 = [-5, 7, -3, 0, 1, 14, 6, 4]
    unsorted_arr_2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(
        f'Merge sort by Algo Monster: {mergesort_algo_monster(unsorted_arr_1)}')
    print(f'Merge sort by Educative: {mergeSort_educative(unsorted_arr_1)}')
