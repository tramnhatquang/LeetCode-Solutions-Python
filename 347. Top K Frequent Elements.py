from collections import *
from typing import *


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		# approach 1: Use a hash map then sort
		# record the occurrences of each number in nums
		# counter = Counter(nums)
		# # sort the counter based on the occurences in the descending order, then returns the first k elements
		# return sorted(counter, key = counter.get, reverse = True)[:k]

		# time: O(n log n), n is the length of nums
		# space: O(n)

		# approach 2: Use heap
		#   1. Keep the occurrences of each number in a table
		#   2. Push  the first k elements to the heap
		#   3. Push the remaining (n-k) elements and pop the least frequent one: O( (n - k) * lg(k)) time. return the heap contents without sorting them: (O(k))
		# time: O((n -k)* log(k))
		# counter = Counter(nums)
		# heap = [(counter[num], num) for num in list(counter.keys())[:k]]
		# heapify(heap)
		# for num in list(counter.keys())[k:]:
		# 	heappushpop(heap, (counter[num], num))
		# return [num for occur, num in heap]

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
