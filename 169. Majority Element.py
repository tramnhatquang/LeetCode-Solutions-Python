class Solution:
	def majorityElement_boyer_moore_voting_algo(self, nums):
		# Use Boyer-Moore voting algo
		count = 0
		candidate = None

		for num in nums:
			if count == 0:
				candidate = num
			if num == candidate:
				count += 1
			else:
				count -= 1

		return candidate

	# time = O(n)
	# space: O(1)

	def majorityElement_counter(self, nums: List[int]) -> int:
		# solve using time O(n) and space O(n)
		# use a counter to count all frequencies and check the condition where counter[val] > n // 2  where n is the length of nums

		counter = Counter(nums)
		n = len(nums)
		for key, val in counter.items():
			if val > n // 2:
				return key  # there is always one majority element in the arr

		return -1  # we need come here but it is a placeholder

	def majorityElement_sort(self, nums):
		nums.sort()
		return nums[len(nums) // 2]

# time: O(nlog n)
# space: O(n)
