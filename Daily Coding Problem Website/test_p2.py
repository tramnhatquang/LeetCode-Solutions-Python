from unittest import TestCase

from p2 import find_product_each_element_1, find_product_each_element_2


class Test(TestCase):
	def test_find_product_each_element_1(self):
		self.assertEqual(find_product_each_element_1([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
		self.assertEqual(find_product_each_element_1([3, 2, 1]), [2, 3, 6])
		self.assertEqual(find_product_each_element_1([-2, -1, 1]), [-1, -2, 2])
		self.assertEqual(find_product_each_element_1([1, 2]), [2, 1])

	def test_find_product_each_element_2(self):
		self.assertEqual(find_product_each_element_2([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
		self.assertEqual(find_product_each_element_2([3, 2, 1]), [2, 3, 6])
		self.assertEqual(find_product_each_element_2([-2, -1, 1]), [-1, -2, 2])
		self.assertEqual(find_product_each_element_2([1, 2]), [2, 1])
