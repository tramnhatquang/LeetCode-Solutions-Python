class Solution:
	def checkIfPangram(self, sentence: str) -> bool:
		counter = Counter(sentence)
		if len(counter) != 26:
			return False

		return True

	def checkIfPangram_other(self, sentence: str) -> bool:
		lst = [0] * 26

		for char in sentence:
			lst[ord(char) - ord('a')] += 1

		return 0 not in lst
