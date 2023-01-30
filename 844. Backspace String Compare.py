class Solution:
	def backspaceCompare_approach_2(self, s: str, t: str) -> bool:

		def build(s: str) -> str:
			res = []
			for char in s:
				if char != '#':
					res.append(char)
				elif res:  # we care the case when # in an empty list
					res.pop()
			return "".join(res)

		return build(s) == build(t)

# time: O(m + n)
# space: O(m + n), m, n are lengths of s, t respectively
