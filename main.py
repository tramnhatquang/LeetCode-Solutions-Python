from bisect import bisect_left


def two_sum(lst, K):
	lst.sort()

	for i in range(len(lst)):
		target = K - lst[i]
		j = binary_search(lst, target)

		# Check that binary search found the target and that it's not in the same index
		# as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
		#  if there's another number that's the same value as lst[i].
		if j == -1:
			continue
		elif j != i:
			return True
		elif j + 1 < len(lst) and lst[j + 1] == target:
			return True
		elif j - 1 >= 0 and lst[j - 1] == target:
			return True
	return False


def binary_search(lst, target):
	lo = 0
	hi = len(lst)
	ind = bisect_left(lst, target, lo, hi)

	if 0 <= ind < hi and lst[ind] == target:
		return ind
	return -1

if __name__ == '__main__':
    assert two_sum([1, -5, 6, 9, 2], 15) is True
