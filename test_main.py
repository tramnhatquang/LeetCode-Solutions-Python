from unittest import TestCase

from main import *


class Test(TestCase):
	def test_max_sum_profit(self):
		self.assertTrue(max_sum_profit([4, 3, -2, 9, -4, 2, 7, 6], 6), 15)
		self.assertTrue(max_sum_profit([-3, 4, 3, -2, 2, 5], 4), 8)
