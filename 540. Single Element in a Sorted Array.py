class Solution:

	def singleNonDuplicate_binar_search(self, nums: List[int]) -> int:

		def to_the_left(index: int) -> bool:
			# Check whether  the current index is already passed the index of single
			# check out of bound
			if index == len(nums) - 1:
				return True
			elif index % 2:  # odd
				return nums[index] != nums[index - 1]
			else:  # even index
				return nums[index] != nums[index + 1]

		left, right = 0, len(nums) - 1
		res = -1
		while left <= right:
			mid = (left + right) // 2
			if to_the_left(mid):  # true means the single element is to the left of the mid index
				res = mid
				right = mid - 1
			else:  # look to the right of the mid index
				left = mid + 1

		# return the single element at the res index
		return nums[res]

	# time: O(log n)
	# space: O(1)

	def singleNonDuplicate_linear_approach(self, nums: List[int]) -> int:
		# use a bitwise XOR operator to find the single element
		ans = 0
		for num in nums:
			ans ^= num

		return ans

# However, it solved the question but not gives us a good time complexity
# time: O(n)
# space: O(1)
