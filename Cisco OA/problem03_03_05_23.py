"""
https://leetcode.com/discuss/interview-question/3216097/CIsco-OA-SHL-Questions
"""


def count_numbers_brute_force(x: int, y: int) -> int:
	"""
	- Given an integer X, write an algorithm to find the number of integers which are less than or equal to X and whose digits add up to Y.
	- Input: an arr of integers
	- Output: print the count of numbers whose digits add up to Y for the given number X. If no number are found, print -1
	"""
	count = 0

	def sum_digit(num: int) -> int:
		total = 0
		while num:
			total += num % 10
			num //= 10
		return total

	for i in range(1, x + 1):
		if sum_digit(i) == y:
			count += 1

	return -1 if count == 0 else count


# time: O(n log n), n is range from 1 to X + 1 (inclusively)
# space: O(1)

# assert count_numbers_optimal(20, 5) == 2
# assert count_numbers_optimal(100, 1) == 3
# assert count_numbers_optimal(2000, 1) == 4
# assert count_numbers_optimal(12, 5) == 1

assert count_numbers_brute_force(20, 5) == 2
assert count_numbers_brute_force(100, 1) == 3
assert count_numbers_brute_force(2000, 1) == 4
assert count_numbers_brute_force(12, 5) == 1
