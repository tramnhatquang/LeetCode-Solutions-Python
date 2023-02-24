from unittest import TestCase

from main import *


class Test(TestCase):
    def test_max_sum_profit(self):
        self.assertTrue(max_sum_profit([4, 3, -2, 9, -4, 2, 7, 6], 6), 15)
        self.assertTrue(max_sum_profit([-3, 4, 3, -2, 2, 5], 4), 8)

    def test_gex_max_aggregate_temperature_change(self):
        self.assertTrue(gex_max_aggregate_temperature_change([-1, 2, 3]), 5)
        self.assertTrue(gex_max_aggregate_temperature_change([-6, -7, -8, 1, -6]), -5)
        self.assertTrue(gex_max_aggregate_temperature_change([6, -2, 5]), 9)
        self.assertTrue(gex_max_aggregate_temperature_change([1, 2, 3, 4, 5]), 15)
        self.assertTrue(gex_max_aggregate_temperature_change([5, 4, 3, 2, 1]), 15)
