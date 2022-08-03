from typing import *


class Solution:
	def bestHand(self, ranks: List[int], suits: List[str]) -> str:
		# approach 1: Hash map + conditions
		#   - Check the set of suit. If the length of the set is equal to 1, we have a 'Flush'
		#   - Check the most common element in the ranks. If its occurrence
		#   >= 3, we have a 'Three of a Kind', else if its occurrence == 2: we have a 'pair', else we have a 'high card'
		if len(set(suits)) == 1:
			return 'Flush'

		counter = Counter(ranks)
		most_common = counter.most_common(1)[0]
		# print(most_common)

		# most_common[1] denotes the freq of the most common value
		if most_common[1] >= 3:
			return 'Three of a Kind'
		elif most_common[1] == 2:
			return 'Pair'
		return 'High Card'

# time = space = O(n), n is the length of ranks = length of the suits
