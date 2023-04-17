from unittest import TestCase

from p4 import find_first_missing_positive_number_1, find_first_missing_positive_number_2


class Test(TestCase):

	def test_find_first_missing_positive_number_2(self):
		self.assertEqual(find_first_missing_positive_number_2([1, 2, 0]), 3)
		self.assertEqual(find_first_missing_positive_number_2([-1, -10, -3]), 1)
		self.assertEqual(find_first_missing_positive_number_2([1, 1, 1, 1, 1, 1, 1, 1]), 2)
		self.assertEqual(find_first_missing_positive_number_2([-1]), 1)
		self.assertEqual(find_first_missing_positive_number_2([0]), 1)
		self.assertEqual(find_first_missing_positive_number_2([-3, -2, -2, -2, 1, 0, 9, 4, 3]), 2)
		self.assertEqual(find_first_missing_positive_number_2([1]), 2)
		self.assertEqual(find_first_missing_positive_number_2([-7, -10, -3, 4, 2, 6, 54, 213]), 1)
		self.assertEqual(find_first_missing_positive_number_2([]), 1)  # if arr is empty, return 1

	def test_find_first_missing_positive_number_1(self):
		self.assertEqual(find_first_missing_positive_number_1([1, 2, 0]), 3)
		self.assertEqual(find_first_missing_positive_number_1([-1, -10, -3]), 1)
		self.assertEqual(find_first_missing_positive_number_1([1, 1, 1, 1, 1, 1, 1, 1]), 2)
		self.assertEqual(find_first_missing_positive_number_1([-1]), 1)
		self.assertEqual(find_first_missing_positive_number_1([0]), 1)
		self.assertEqual(find_first_missing_positive_number_1([-3, -2, -2, -2, 1, 0, 9, 4, 3]), 2)
		self.assertEqual(find_first_missing_positive_number_1([1]), 2)
		self.assertEqual(find_first_missing_positive_number_1([-7, -10, -3, 4, 2, 6, 54, 213]), 1)
		self.assertEqual(find_first_missing_positive_number_1([]), 1)  # if arr is empty, return 1
