from collections import Counter


class Solution:
	def findPairs_optimal(self, nums: List[int], k: int) -> int:
		"""
		- The optimal solution: Using a hash map and traverse thr the hash map and count the required pairs
			- If there is a key in the hash map which is equal to (x + k) if k >0 , we increase the count (i.e. if we found a pair (1, 4) and k = 3, we wont count (4, 1))
			- If there is more than one occurrence of x if k == 0, we increase the count
		"""
		count = 0
		counter = Counter(nums)

		for num in counter:
			if k > 0 and num + k in counter:
				count += 1
			elif k == 0 and counter[num] > 1:
				count += 1

		return count

	# time: O(n), n is length of arr
	# space: O(1)

	def findPairs_brute_force(self, nums: List[int], k: int) -> int:
		"""
		 - Brute force solution: find all pairs whose absolute diff = k and store these pairs into a set to get all unique pairs
		- To avoid duplicate, we can sort the arr first.
		- Then in a nested loop, no matter it is a inner or outer loop, we move on to the next number if the curr number is the same Las the prev number
		"""
		nums.sort()
		count = 0
		n = len(nums)
		for i in range(n - 1):
			# avoid duplicate
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, n):
				# avoid duplicate
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue

				if nums[j] - nums[i] == k:
					count += 1
		return count
# time: O(n^2)
# space: O(n)
