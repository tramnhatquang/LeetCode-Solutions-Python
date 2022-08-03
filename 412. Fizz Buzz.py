from  typing import List
class Solution:
	def fizzBuzz(self, n: int) -> List[str]:
		# Time: O(n)
		# Space: O(1) if we ignore the space taken by the output
		res = []

		for i in range(1, n + 1):
			if i % 3 == 0 and i % 5 == 0:
				res.append('FizzBuzz')
			elif i % 3 == 0:
				res.append('Fizz')
			elif i % 5 == 0:
				res.append('Buzz')
			else:
				res.append(str(i))

		return res

		# Using an ordered hash tbale to make the code neat
		res = []

		hash_map = {3: 'Fizz', 5: 'Buzz'}

		for i in range(1, n + 1):
			num_t_str = ''

			for key in hash_map:
				if i % key == 0:
					num_t_str += hash_map[key]

			if not num_t_str:
				num_t_str = str(i)
			res.append(num_t_str)

		return res