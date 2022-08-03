class Solution:
	def trap(self, height: List[int]) -> int:
		# The concept here is water that is going to get stored above any building would depenf upon largest height of building to it's left
		# and also the largest height of building to it's right. You take the minimum of it as only till that height the water would accumulate
		# Now just subtract of height of the building you are currently at so you get the heeight of water above it.

		# APPROACH 1: Find the maxleft and maxRight height of the current index and use the formula
		# water[i] denotes the water can trapped at the current index
		# water[i] = min(maxLeft, maxRight) - height[i]
		# where maxLeft denotes the  highest bar to the left of the current bar (not including)
		# where  maxRight denotes the  highest bar to the right of the current bar (not including) and height[i] denotes the current height of the current bar

		# after that, we use the above formula to compute the water trapped by each index. The result is the sum of all trapped water

		#         ans = 0
		#         n = len(height)
		#         max_left = n * [0]
		#         max_right  = n * [0]

		#         for i in range(1, n):
		#             max_left[i] = max(height[i - 1], max_left[i - 1])

		#         for i in range(n - 2, -1, -1):
		#             max_right[i] = max(height[i + 1], max_right[i + 1])

		#         # compute all the trapped water
		#         for i in range(n):
		#             water_level = min(max_left[i], max_right[i])
		#             if water_level > height[i]:
		#                 ans += water_level - height[i]

		#         return ans

		# time: O(N) where N is the length of the input
		# space: O(N)

		# APPROACH 2: Two pointers technique that can reduce thespace complexity to O(1)

		if not height:
			return 0

		volume = 0
		left, right = 0, len(height) - 1
		l_max, r_max = height[left], height[right]
		while left < right:
			l_max, r_max = max(height[left], l_max), max(height[right], r_max)
			if l_max <= r_max:
				volume += l_max - height[left]
				left += 1
			else:
				volume += r_max - height[right]
				right -= 1
		return volume
