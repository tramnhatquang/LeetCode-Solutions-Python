import collections


def find_majority_element(nums):
	# TODO: Write your code here
	counter = collections.Counter(nums)
	num_len = len(nums)
	for num, freq in counter.items():
		if freq > (num_len // 2):
			return num  # return the number whose freq > len // 2

	return -1


# time: O(n), space: O(n)


def find_majority_element(nums):
	candidate = None
	count = 0
	for num in nums:
		if count == 0:
			candidate = num
		elif num == candidate:
			count += 1
		else:
			count -= 1
	return candidate
