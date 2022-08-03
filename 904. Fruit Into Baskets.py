from collections import *
from typing import *


class Solution:
	def totalFruit(self, fruits: List[int]) -> int:
		# approach: the problem can be phrased as find the max length of the subarray containing at most two distinct characters

		# 1. Keep a sliding window going from left to right. It is formed by a left and right pointer
		# 2. Sliding window contains at most two distinct characters. If we have more than two, we shrink the sldiing window by moving the left pointer by one, and also decrement it ocurrence. If its occurence is equal to 0, we remove that character from the freq table. We keep track of the max length so far whenever we have at most two distinct characters. (max length = length of the sliding window)
		if not fruits:
			return 0

		freq_table = defaultdict(int)
		left = max_length = 0

		# extending the [left, right]
		for right in range(len(fruits)):
			right_char = fruits[right]
			freq_table[right_char] += 1

			if len(freq_table) > 2:
				freq_table[fruits[left]] -= 1
				if freq_table[fruits[left]] == 0:
					del freq_table[fruits[left]]

				left += 1

			max_length = max(max_length, right - left + 1)
		return max_length

# time: O(N), N IS THE LENGTH OF FRUITS
# SPACE: O(1), SINCE THE TABLE CONTAINS AT MOST TWO DISTINCT CHARACTERS
