class Solution:
	def countElements(self, arr: List[int]) -> int:
		num_set = set(arr)
		count = 0
		for num in arr:
			if num + 1 in num_set:
				count += 1

		return count


# time: O(n) = space
1
