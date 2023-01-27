class Solution:
	def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

		n = len(releaseTimes)
		# sanity check
		if n == 1:
			return keysPressed[0]

		# Notice that the duration of each char = releaseTimes[i] - releaseTimes[i - 1] if i > 0
		longest_duration = releaseTimes[0]
		slowestKey = keysPressed[0]
		for i in range(1, n):
			current_duration = releaseTimes[i] - releaseTimes[i - 1]
			if current_duration > longest_duration:
				longest_duration = current_duration
				slowestKey = keysPressed[i]
			# we have find lexicographically largest key of the keypresses.
			elif current_duration == longest_duration:
				slowestKey = max(slowestKey, keysPressed[i])

		return slowestKey
# time: O(n)
# space: O(1)
