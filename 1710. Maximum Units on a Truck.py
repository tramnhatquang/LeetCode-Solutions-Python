from typing import Counter, List


class Solution:

	def maximumUnits_counting_sort(self, boxTypes: List[List[int]], truckSize: int) -> int:
		boxes, cur_units, cnt = 0, 1000, Counter()
		for box, units in boxTypes:
			cnt[units] += box
		while cur_units > 0:
			if cnt[cur_units] > 0:
				fit_in = min(truckSize, cnt[cur_units])
				boxes += fit_in * cur_units
				truckSize -= fit_in
				if truckSize == 0:
					return boxes
			cur_units -= 1
		return boxes

	def maximumUnits_sort(self, boxTypes: List[List[int]], truckSize: int) -> int:
		# greedy algorithm
		# sort all the boxes by their units in the reversed order
		# starting with the highest unnit, try to get as much as possible boxes. If I still have space, go to the second highest unit. COntinue doing so until I run out of space

		boxTypes.sort(key=lambda x: -x[1])
		count = 0
		for box, unit in boxTypes:
			count += min(box, truckSize) * unit
			truckSize -= box
			if truckSize <= 0:
				break

		return count


# time: O(n log n) due to Timsort
# space: O(n)


if __name__ == '__main__':
	s = Solution()
	s.maximumUnits([[1, 3], [2, 2], [3, 1]], 4)
