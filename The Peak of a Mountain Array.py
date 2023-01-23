class Solution:
	def peakIndexInMountainArray_optimal(self, arr: List[int]) -> int:
		# use binary search to find the peak index
		# We already know the array strictly decreases from the peak element to the last element. So we can try to use a feasible function of arr[i]> arr[i+1] to return true for elements from the peak to the last element. Once we do that, we realize that also returns false from the first element to the peak element. We got our feasible function.
		# A minor edge case is for the last element as it has no next element. We can pad the array with an imaginary node of negative infinity. In the implementation, we don't actually need to pad the array as that would incur O(n) extra cost. We can just check if i+1 is out of bounds and return true if it is.

		n = len(arr)
		left, right = 0, n - 1
		boundary_index = -1
		while left <= right:
			mid = (left + right) // 2
			# search to the left space, since mid can be a peak
			if mid == n - 1 or arr[mid] > arr[mid + 1]:
				boundary_index = mid
				right = mid - 1
			else:
				left = mid + 1

		return boundary_index

	# time: O(log n)
	# space: O(1)
	def peakIndexInMountainArray_linear(self, arr: List[int]) -> int:
		n = len(arr)
		if n < 3:
			return -1  # must have at least 3 elements

		# find the peak by moving along the arr
		index = 0
		while index + 1 < n and arr[index] < arr[index + 1]:
			index += 1
		return index

# time: O(n / 2) = O(n), n is length of arr
# spacE: O(1)
