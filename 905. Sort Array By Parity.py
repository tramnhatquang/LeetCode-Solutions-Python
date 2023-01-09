import collections
from typing import *


class Solution:

	def sortArrayByParity(self, nums: List[int]) -> List[int]:
		arr = collections.deque()
		for num in nums:
			if num % 2 == 0:
				arr.appendleft(num)
			else:
				arr.append(num)

		return list(arr)

	# time = space = O(n)
	# we do only one pass traversal through the list
	def sortArrayByParity_1(self, nums: List[int]) -> List[int]:
		arr = []
		for num in nums:
			if num % 2 == 0:
				arr.append(num)

		for num in nums:
			if num % 2 != 0:
				arr.append(num)

		return arr

	# time = space = O(n)
	# we do two passes traversal through the list