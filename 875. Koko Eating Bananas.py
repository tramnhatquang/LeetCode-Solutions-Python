class Solution:
	def minEatingSpeed_optimal(self, piles: List[int], h: int) -> int:
		left, right = 1, max(piles)
		res = -1
		while left <= right:
			mid = (left + right) // 2
			expected_time = 0

			# see if Koko can eat all bananas with a speed of mid within h hours
			for pile in piles:
				expected_time += math.ceil(pile / mid)

			if expected_time <= h:
				res = mid  # mid could be a potential speed
				right = mid - 1
			else:
				left = mid + 1

		return res

	# time: O(n * log m), m is the max number of bananas in a single pile from piles and n is the length of the input arr
	# space: O(1)

	def minEatingSpeed_linear_approach(self, piles: List[int], h: int) -> int:
		# linear approach
		# starting from 1 and see if Koko can eat all bananas within the timeframe h. If it does not, increase k by 1 and keep doing so until we satisfy the rquirements
		# do a stimulation
		k = 1

		while True:
			expected_time = 0
			for pile in piles:
				expected_time += math.ceil(pile / k)

			# check if Koko can eat all bananas within the h hours
			if expected_time <= h:
				return k
			else:
				k += 1

# time: O(n) -> TLE
# space: O(1)
