class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		n = len(digits)
		if n == 0:  # sanity check
			return []

		res = []
		map = {
				'2': 'abc',
				'3': 'def',
				'4': 'ghi',
				'5': 'jkl',
				'6': 'mno',
				'7': 'pqrs',
				'8': 'tuv',
				'9': 'wxyz'
		}

		def backtrack(path: List[str], index: int) -> None:
			# base case
			if len(path) == n:
				res.append(''.join(path))
				return

			# get all letters that the current digit maps to, and loops through that
			letters = map[digits[index]]
			for letter in letters:
				path.append(letter)
				# move on to the next digits
				backtrack(path, index + 1)
				# backtrack by removing the letter before moving onto the next
				path.pop()

		backtrack([], 0)
		return res

# Algo:
# Basically, we will lock in each digit in the string. try all possbile combinations of each character in the first digit to the second one and so on
# 1. If the input is empty, return an empty array.
# 2. Initialize a data structure (e.g. a hash map) that maps digits to their letters, for example, mapping "6" to "m", "n", and "o".
# 3. Use a backtracking function to generate all possible combinations.
#   - The function should take 2 primary inputs: the current combination of letters we have, path, and the index we are currently checking.
#   - As a base case, if our current combination of letters is the same length as the input digits, that means we have a complete combination. Therefore, add it to our answer, and backtrack.
#   - Otherwise, get all the letters that correspond with the current digit we are looking at, digits[index].
#   - Loop through these letters. For each letter, add the letter to our current path, and call backtrack again, but move on to the next digit by incrementing index by 1.
#   - Make sure to remove the letter from path once finished with it.

# time: O(n * 4^n), n is length of digits, 4 refers to the max value length in the hash map
# spacE: O(n), n is length of digits
