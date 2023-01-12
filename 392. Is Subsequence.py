class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		n, m = len(s), len(t)
		if n > m:
			return False
		elif n == m:
			return s == t

		# use two pointers technique
		# Each pointer points at the first index of each string
		# Do a while loop until one of pointers reach its end
		# Inside the loop, we compare chars from both string, if we have  match, we move two pointers at the same time. If we have a mismatch, we move the pointer of the t string.

		# Outside the loop, we check if pointer of s string == len(s)
		p1 = p2 = 0
		while p1 < n and p2 < m:
			if s[p1] == t[p2]:
				p1 += 1
			p2 += 1

		return p1 == n

# time: O(n + m), where n, m are lengths of s, t respectively
# space: O(1)

