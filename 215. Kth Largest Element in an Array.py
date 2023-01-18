import heapq
from typing import List


class Solution:

	def findKthLargest_own_heap(self, nums: List[int], k: int) -> int:
		# use a min heap tp solve it
		n = len(nums)
		if n < k:
			return -1  # invalid

		heap = []
		for num in nums:
			if len(heap) < k:
				heapq.heappush(heap, num)
			else:
				if num > heap[0]:
					heapq.heappushpop(heap, num)

		return heap[0]

	# time: O(n log k)
	# space: O(k)

	def findKthLargest_built_in_solution(self, nums: List[int], k: int) -> int:
		# use a heap to return k-th largest element

		# conver arr to a heap
		heap = nums
		heapq.heapify(heap)  # O(n)

		# return the k-th largest element in heapq.nlargest(k, heap)[-1]
		return heapq.nlargest(k, heap)[-1]

	# time: O(n * log(k))
	# space: O(n) to convert the whole arr to a heap

	def findKthLargest_sort(self, nums: List[int], k: int) -> int:
		# the brute force solution
		# sort the whole arr in the descending order then return the element at nums[k-1]
		nums.sort(reverse=True)
		return nums[k - 1]
# time: O(n log n )
# space: O(n)
