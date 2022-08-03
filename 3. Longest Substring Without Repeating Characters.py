class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		# approach 1: find every possible substrings and use a variable to keep track of the current longest length among the ones with non-repeating characters
		# TC for find every possible substrings is O(n^2)
		# TC to check if any substrings are the ones with non-repeating characters is O(n)
		# total TC: O(n^3), space: O(n)

		# longest_length = 0
		# for i in range(len(s)):
		#     for j in range(i, len(s)):
		#         if len(s[i:j+1]) == len(set(s[i:j+1])):
		#             longest_length = max(longest_length, j - i + 1)
		# return longest_length

		# However, this approach is TLE. Can we optimize the TC ?

		# Approach 2: Using the sliding window technique. We need to use a hash map to keep track of both character and the last index of that character we have so far. Whenever we have a duplicate character, we'll shrink the our sliding window to make sure that we only have distinct characters within the sliding window
		window_start = 0
		max_length = 0  # the smallest
		char_index_map = {}

		for window_end in range(len(s)):
			right_char = s[window_end]
			# if the map already contains the 'right_char', shrink the window from the beginning so that
			# we have only one occurrence of 'right_char'
			if right_char in char_index_map:
				# this is tricky; in the current window, we will not have any 'right_char' after its previous index
				# and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
				window_start = max(window_start, char_index_map[right_char] + 1)
			# window_start = char_index_map[right_char] + 1

			# insert the 'right_char' into the map
			char_index_map[right_char] = window_end
			# remember the maximum length so far
			max_length = max(max_length, window_end - window_start + 1)
		return max_length
# time: O(n), space: O(m), n is the length of the input, m is the
# size of unique characters
