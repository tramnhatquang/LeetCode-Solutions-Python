class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:
		# brute force Solution
		# check every possible subarray whose lengths are equal to k
		# record the max average so far and return it
		res = 0
		for i in range(len(nums) - k + 1):
			# calculate the average of each subarray and record the max
			avg = sum(nums[i:i + k]) / k
			res = max(res, avg)

		return res

	# time (TLE):O(n^2), space: O(n), not efficient, where n is length of nums

	def findMaxAverage_optimal(self, nums: List[int], k: int) -> float:
		# use the sliding window technique
		# build our initial window whose length == k

		# left, right pointers are bounds of the window
		# whenever the window length > k then we remove the left number. Otherwise, we find the avg of each subarray and record the max so far

		# build our initial window
		max_sum = curr = sum(nums[:k])
		for i in range(k, len(nums)):
			curr += nums[i] - nums[i - k]
			max_sum = max(curr, max_sum)

		return max_sum / k
# time: O(n), space:O(k)
