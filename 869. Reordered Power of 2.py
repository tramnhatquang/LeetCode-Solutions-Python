class Solution:
	def reorderedPowerOf2(self, n: int) -> bool:
		# count all the power of 2 since 1 <= n <= 10^9, so up to 8 same digits
		# if n > 10^9, we can use a hash map
		# we use a counter to count the number of digits 9876543210 in the given number
		counter = collections.Counter(str(n))
		return any(counter == collections.Counter(str(1 << i)) for i in range(30))
