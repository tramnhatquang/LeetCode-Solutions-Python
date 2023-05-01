'''
Link: https://leetcode.com/problems/slowest-key/
'''


class Solution:
	def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
		'''
		- Can I assume length of releaseTimes and keysPressed are the same? Do we have valid input? If we dont, how do you want to handle?
		- releaseTimes[i] denotes the time in which the keysPressed[i] was pressed. We have to find key that has the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.

		'''
		largest_key = 'a'
		longest_duration = 0
		n = len(keysPressed)
		for i in range(n):
			pressedTime = releaseTimes[i - 1] if i > 0 else 0
			current_duration = releaseTimes[i] - pressedTime
			if current_duration == longest_duration:
				# update the max lexicographically character
				largest_key = max(largest_key, keysPressed[i])
			elif current_duration > longest_duration:
				longest_duration = current_duration
				largest_key = keysPressed[i]

		return largest_key

# time: O(n), n is length of keypresses arr
# space: O(1)
