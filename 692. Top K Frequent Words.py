from collections import Counter
from heapq import *
from typing import *


class Solution:

	def topKFrequent_max_heap(self, words: List[str], k: int) -> List[str]:
		"""
		Solve using a max heap to optimize the time complexity
		- count each word and its freq then store them into a hash map
		- convert the stored arr into a max heap (based on the freq then the lexicographical order of words)
		- Pop the first k words from the max heap and that's our desired output
		"""
		counter = Counter(words)
		heap = [(-freq, word) for word, freq in counter.items()]

		# convert into a max heap
		heapify(heap)  # takes O(n)

		# return the top k elements from the max heap
		return [heappop(heap)[1] for _ in range(k)]


# time: O(n + nlogk)
# space: O(N) used to store the counter, O(k) space is for the heap


def topKFrequent(self, words, k):
	# Step 1: Count the frequency of each word using a dictionary
	frequency = Counter(words)

	# Step 2: Create a list of tuples, where each tuple contains a word and its frequency
	word_freq_list = [(word, freq) for word, freq in frequency.items()]

	# Step 3: Sort the list based on the frequency and lexicographic order
	sorted_word_freq_list = sorted(word_freq_list, key=lambda x: (-x[1], x[0]))

	# Step 4: Return the first k words from the sorted list
	return [word for word, _ in sorted_word_freq_list[:k]]


"""
- time: O(n log n), n is length of words
- space: O(n), the space used to store frequency, and return a slice from a sorted list of length O(n)
"""
