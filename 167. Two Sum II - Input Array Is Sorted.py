from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time: O(n) where n is the length of numbers
        # Space: O(n) since the table's size stores up to the most n elements

        # hash_table = {}
		#
        # for index, number in enumerate(numbers):
        #     complement = target - number
        #     if complement in hash_table:
        #         return [hash_table[complement], index + 1]
        #     hash_table[number] = index + 1

        # Time: O(n) where n is the length of numbers
        # Space: O(1) since we do not use any extra variables
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

