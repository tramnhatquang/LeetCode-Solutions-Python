class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		if k <= 1:
			return 0

		# use the sliding window technique
		left = ans = 0
		curr_product = 1

		for right in range(len(nums)):
			curr_product *= nums[right]
			while curr_product >= k:
				curr_product //= nums[left]
				left += 1

			# the trick part is that the newly created arr for each index is equal to right - left + 1 which is window length
			ans += right - left + 1

		return ans
		# time: O(n), space: O(1), n is the length of nums
