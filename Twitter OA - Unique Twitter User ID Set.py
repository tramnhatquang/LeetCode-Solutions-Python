from collections import Counter
from typing import List


def get_sum_optimal(l: List[int]) -> int:
	total = 0
	elements = Counter(l)
	min_element = min(l)
	max_element = max(l)
	for i in range(min_element, max_element):
		if i in elements:
			total += i
			if elements[i] > 1:
				if (i + 1) in elements:
					elements[i + 1] += elements[i] - 1
				else:
					elements[i + 1] = elements[i] - 1
	if max_element in elements:
		total += (2 * max_element + elements[max_element] - 1) * elements[max_element] // 2
	return total


# time: O(n + m), n is length of arr, m is the maximum element size
# space: O(n + m)

def get_sum_better_sorting(arr: List[int]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	arr.sort()
	total = arr[0]  # append the first number since it is first unique number
	n = len(arr)
	for i in range(1, n):
		if arr[i - 1] >= arr[i]:
			arr[i] = arr[i - 1] + 1
		total += arr[i]
	return total


# time: O(n log n)
# space: O(n)


def get_sum_non_optimal(arr: List[int]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	"""
	- The brute force solution is try all numbers in the arr and check there are no duplicates.
	If there is a duplicate, we increase the number until it is unique. We repeat the process until
	all numbers are unique
	"""
	total = 0
	used_num = set()
	for num in arr:
		while num in used_num:
			num += 1
		total += num  # add number when it is unique
		used_num.add(num)
	return total


# time: O(n^2), n is length of arr
# space: O(n) for used set

if __name__ == '__main__':
	input = [1, 2, 2, 3, 4]
	output = get_sum_optimal(input)
	print(output)
