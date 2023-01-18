import collections
import heapq
from collections import *
from typing import *


class Solution:

	def topKFrequent_optimal_bucket_count(self, nums: List[int], k: int) -> List[int]:
		# approach 3: Bucket sort
		# no frequencies is more than n (n is the length of the input)
		# using a table where key is the number of occurrence, and val is the list of numbers that have the same occurrence
		bucket = [[] for _ in range(len(nums) + 1)]
		count = Counter(nums).items()
		for num, freq in count:
			bucket[freq].append(num)

		# loop backward from the freq table and store k elements into the result list
		res = []
		for i in range(len(bucket) - 1, 0, -1):
			for num in bucket[i]:
				res.append(num)
				if len(res) == k:
					return res

	# time: O(n) = space, n is the length of the input
	def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:

		n = len(nums)
		if k == n:
			return nums
		# 1. build hash map : character and how often it appears
		# O(N) time
		count = collections.Counter(nums)
		# 2-3. build heap of top k frequent elements and
		# convert it into an output array
		# O(N log k) time
		return heapq.nlargest(k, count.keys(), key=count.get)

	# return [num for occur, num in heap

	def topKFrequent_built_in_solution(self, nums: List[int], k: int) -> List[int]:

		# approach 1: Use a hash map then sort
		# record the occurrences of each number in nums
		# counter = Counter(nums)
		# # sort the counter based on the occurences in the descending order, then returns the first k elements
		return [x for x, y in collections.Counter(nums).most_common(k)]

# time: O(n log n), n is the length of nums
# space: O(k)
