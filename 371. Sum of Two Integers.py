class Solution:

	def getSum_easy_approach_python_implementation(self, a: int, b: int) -> int:
		"""
		This approach can only be used for Java implementation

		"""
		mask = 0xFFFFFFFF

		while b != 0:
			a, b = (a ^ b) & mask, ((a & b) << 1) & mask

		max_int = 0x7FFFFFFF
		return a if a < max_int else ~(a ^ mask)

	# time= space = O(1)
	def getSum_easy_approach_java_implementation(self, a: int, b: int) -> int:

		while b != 0:
			a, b = (a ^ b), ((a & b) << 1)

		return a

	# time= space = O(1)

	def getSum_cheat_approach(self, a: int, b: int) -> int:
		return a + b


# time: O(1) = space, but not accepted since I cannot use + or - in the Solution


mask = 0xFFFFFFFF
print(mask)
