'''
Link to problem: https://algo.monster/problems/fill_the_truck
'''
from typing import *


class Solution:
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		# sort all boxes  based on the number of units per box
		# fill the truck with as many as higher number of units per box until the truck is full

		# make sure that the list is sorted based on the number of units per box in reversed order
		boxTypes.sort(key=lambda x: -x[1])
		max_unit = 0
		for num, unit in boxTypes:
			if truckSize <= 0:
				break
			# if we have enough space for the current unit
			max_unit += min(num, truckSize) * unit
			truckSize -= num

		return max_unit

	'''
	time:O(n log n) due to sorting
	space: O(n)
	'''
