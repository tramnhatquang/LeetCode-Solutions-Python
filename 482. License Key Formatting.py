class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		# replace all the '-' by '' and then upper all the chracters and reverse it
		new_string = s.replace('-', '').upper()[::-1]
		lst_string = []
		for i in range(0, len(new_string), k):
			lst_string.append(new_string[i:i + k])
		return '-'.join(lst_string)[::-1]

# time: O(n), space: O(n)
