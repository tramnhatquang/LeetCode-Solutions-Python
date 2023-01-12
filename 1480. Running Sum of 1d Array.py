class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		for i in range(1, len(nums)):
			nums[i] += nums[i - 1]

		return nums

	# time: o(n), space: o(1)

	def runningSum_alternative(self, nums: List[int]) -> List[int]:
		running_sum = 0

		for i in range(len(nums)):
			running_sum += nums[i]
			nums[i] = running_sum

		return nums
