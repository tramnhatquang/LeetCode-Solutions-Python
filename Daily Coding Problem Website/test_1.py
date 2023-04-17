from unittest import TestCase

from p1 import find_two_numbers


class Test(TestCase):
	def test_find_sum(self):
		# assert True

		self.assertTrue(find_two_numbers([10, 15, 3, 7], 17))
		self.assertTrue(find_two_numbers([1, 2], 3))

		# assert False
		self.assertFalse(find_two_numbers([1, 2, 3], 10))
		self.assertFalse(find_two_numbers([1, 1, 1], 1))
