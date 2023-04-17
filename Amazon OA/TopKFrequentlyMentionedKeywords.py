from collections import Counter


class Solution:

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
