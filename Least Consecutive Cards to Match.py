from collections import defaultdict
from typing import List


def least_consecutive_cards_to_match(cards: List[int]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	# the question is something similar to find the shortest sliding window that has a duplicate
	left = 0
	length = len(cards) + 1
	window = defaultdict(int)

	for right in range(len(cards)):
		window[cards[right]] += 1
		while window[cards[right]] == 2:
			length = min(length, right - left + 1)
			window[cards[left]] -= 1
			left += 1

	return length if length != len(cards) + 1 else -1
