from typing import List


class Solution:
	def fillCups(self, amount: List[int]) -> int:
		# approach 1: To minimize the amount of time needed, you want to fill up as many cups as possible in each second. This means that you want to maximize the number of seconds where you are filling up two cups.
		# You always want to fill up the two types of water with the most unfilled cups.
		# observations:
		#   - res >= max(amount). For each time, you can reduce one type at most one cup, so the final result is bigger or equal to max(amount)
		#   - res >= ceil(sum(amount) / 2). For each second, you can fill up to two cups so the final result is bigger or equal to ceil(sum(A) / 2). The optimal strategy is always to fill two different cups as long they are available. The first thing to notice is that one of the two cups will always be from the biggest stack. The other cup will come from the smallest and medium stack depending on which one is still available. In fact - there is no difference between the smallest and the medium stack because you can take either of them, exhaust it and proceed to the remaining stack - all the while also taking cups from the biggest stack

		return max(max(amount), (sum(amount) + 1) // 2)
# time: O(n), space: O(1) , n is the length of the amount
