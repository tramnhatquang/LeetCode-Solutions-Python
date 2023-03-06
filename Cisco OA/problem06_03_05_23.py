"""
https://leetcode.com/discuss/interview-question/3216097/CIsco-OA-SHL-Questions
"""
from collections import Counter
from typing import *


def check_twin(arr: List[int]) -> int:
	counter = Counter(arr)
	for num in arr:
		if counter[num] == 1:
			return num

	return -1


assert check_twin([1, 1, 2, 3, 3, 4, 4]) == 2
assert check_twin([1, 1, 2, 2]) == -1
assert check_twin([1, 3, 4, 2]) == 1
assert check_twin([1, 1, 2, 2, 3, 4]) == 3
assert check_twin([2, 5, 6, 2, 4, 6, 5, 4]) == -1
