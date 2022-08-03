from typing import *

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		# approach 1: brute force solution (Set to check duplicat)
		# loop over the given arr, add each number to the set if that number has not been in the set. If one number is already in the set, that is our duplicate number
		# time = space = O(n), n is the length of nums
		visited = set()
		for num in nums:
			if num in visited:
				return num
			visited.add(num)

		# however, the problem specifically said that we must optimize the problem to O(1) space

		# approach 2: cyclic sort (used only when the input is in specific range. In this case, all elements are in range [1, n] inclusive.
		# that means 1 goes to 0-index, 2 goes to 1-index, so on and so fourth. So, for each index in the given arr after swapping, if the index + 1 != nums[index], the nums[index] is our duplicate
		# we solve this problem in one pass
		# pass 1: traversing the arr and put each number to its associated index where nums[i] == i + 1. If the current number at index i is not put at the correct index, we swap the number with the number at its correct index. If both numbers are the same, we find a duplicate. We will not move on to the next index until the number is placed at its correct index

		#         n = len(arr)
		#         i = 0
		#         while i < n:
		#             # there is a wrong number placed at this index
		#             # 1 -> 0-index, 2 -> 1-index
		#             if nums[i] != i + 1:
		#                 # the correct index
		#                 correct_index = nums[i] - 1
		#                 if nums[i] != nums[correct_index]:
		#                     # swap
		#                     nums[i], nums[correct_index] = nums[correct_index], nums[i]
		#                 else:
		#                     # the number at this index is equal to the number at this correct index. It means nums[i] is the duplicate number
		#                     return nums[i]
		#             else:
		#                 i += 1

		#         return -1

		# approach 3: fast and slow pointer
		# 1. find the intersection point between the fast and slow pointers. Fast advances by 2, while slow advances by 1.
		# 2. Find the starting point of the cycle (the duplicate number). Initialzing another slow pointer starting from the head. Both advancing two slow pointers until they meet.
		slow = fast = 0
		while True:
			fast = nums[nums[fast]]
			slow = nums[slow]
			if fast == slow:
				break

		slow2 = 0
		while True:
			slow2 = nums[slow2]
			slow = nums[slow]
			if slow == slow2:
				return slow

	# time: O(n), space: O(1)
