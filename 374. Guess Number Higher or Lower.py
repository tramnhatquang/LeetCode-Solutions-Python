# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
	def guessNumber_optimal(self, n: int) -> int:
		# optimal solution is to use BS on the range from 1 to n
		left, right = 1, n
		while left <= right:
			# At here, mid denotes the index and also the number from 1 to n
			mid = (left + right) // 2
			if guess(mid) == 0:
				return mid
			# search the right space (mid < picked number)
			elif guess(mid) == 1:
				left = mid + 1
			# search the left space (mid > picked number)
			else:
				right = mid - 1

		return -1  # we never return this, just a placeholder

	def guessNumber(self, n: int) -> int:
		# brute force Solution
		# try all numbers from 1 to n inclusively and call the given API on that number
		# whenever the APi returns 0- > return that number
		# otherwise, returns -1

		for i in range(1, n + 1):
			if guess(i) == 0:
				return i
		return -1

# time: O(n) n is length from 1 to n -> gives us a TLE
# space: O(1)
