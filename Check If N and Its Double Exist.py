class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		num_set = set()

		for num in arr:
			if num * 2 in num_set or num / 2 in num_set:
				return True

			# if num % 2 == 0 and num // 2 in num_set:
			# 	return True

			# we can replace num % 2 == 0 and num // 2 as num /2
			# in Python , // is an integer division, while / is a float division
			# if num is odd, / will lead to a float, and if num is even,
			# / is an integer number

			# so we can do something like this

			# else
			num_set.add(num)

		return False

	# time: O(n), space: O(n)
