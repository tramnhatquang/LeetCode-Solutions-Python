import heapq


class Solution:
	def halveArray(self, nums: List[int]) -> int:
		# sicne we want to minimize number of operations -> it also means we have to maximize the amount we reduce nums at each iteration
		# This means at any given moment, we should choose the largest element. To track the largest element at any given time, let's convert the input into a max heap.
		target = sum(nums) / 2
		heap = [-num for num in nums]

		# convert into a max heap
		heapq.heapify(heap)

		ans = 0
		while target > 0:
			ans += 1
			x = heapq.heappop(heap)
			target += x / 2  # remove x/2 from the sum
			heapq.heappush(heap, x / 2)  # push x/2 back onto the heap

		return ans

# time: O(n log n)
# space: O(n)
