"""
Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals


There is a small caveat: if there is no element in the array whose square equals n, then we want to return the largest element that is smaller than n. In this case, we are actually looking for the last false. We can subtract 1 from the index after we find the first true from binary search.
"""


def square_root(n: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	if n == 0:
		return 0

	left, right = 1, n
	res = -1
	while left <= right:
		mid = (left + right) // 2
		if mid * mid == n:
			return mid
		elif mid * mid > n:
			res = mid
			right = mid - 1
		else:
			left = mid + 1
	return res - 1


# time: O(log n)
# space: O(1)

if __name__ == '__main__':
	assert square_root(4) == 2
	assert square_root(8) == 2
	assert square_root(10) == 3
	assert square_root(0) == 0
	assert square_root(1) == 1
