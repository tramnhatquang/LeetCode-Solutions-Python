class Solution:

	def sortArray_merge_sort(self, nums: List[int]) -> List[int]:

		def merge_sort(nums: List[int]) -> List[int]:
			if len(nums) > 1:
				mid = len(nums) // 2
				left = nums[:mid]
				right = nums[mid:]

				# recursive call on each half
				merge_sort(left)
				merge_sort(right)

				# two iterators for traversing the two halves
				i = j = 0
				# iterator for the main list
				k = 0
				while i < len(left) and j < len(right):
					if left[i] <= right[j]:
						nums[k] = left[i]
						i += 1
					else:
						nums[k] = right[j]
						j += 1
					k += 1

				# for all the remaining values
				while i < len(left):
					nums[k] = left[i]
					i += 1
					k += 1
				while j < len(right):
					nums[k] = right[j]
					j += 1
					k += 1

			return nums

		return merge_sort(nums)
	# time: O(n log n), n is length of arr
	# space: O(n)


def sortArray_cheat(self, nums: List[int]) -> List[int]:
	"""
	Cheat way, using the built-in sort in Python
	- Time: O(n log n), n is length of nums
	- Space: O(n)
	"""
	nums.sort()
	return nums
