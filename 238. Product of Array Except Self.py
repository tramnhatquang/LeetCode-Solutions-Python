from typing import *


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		# approach 1: O(1) space approach Initialize the empty answer array
		# where for a given index i, answer[i] would contain the product of
		# all the numbers to the left of i. We construct the answer array the
		# same way we constructed the L array in the previous approach. These
		# two algorithms are exactly the same except that we are trying to
		# save up on space. The only change in this approach is that we don't
		# explicitly build the R array from before. Instead, we simply use a
		# variable to keep track of the running product of elements to the
		# right and we keep updating the answer array by doing answer[i] =
		# answer[i] * R answer[i]=answer[i]∗R. For a given index i, answer[i]
		# contains the product of all the elements to the left and R would
		# contain product of all the elements to the right. We then update R
		# as R = R * nums[i]R=R∗nums[i]
		n = len(nums)
		res = [1] * n

		for i in range(1, n):
			res[i] = res[i - 1] * nums[i - 1]

		right = 1
		for i in range(n - 2, -1, -1):  # traverse backward
			right *= nums[i + 1]
			res[i] *= right

		print(res)
		return res

# time: O(n), space: O(1) if we ignore the output space
