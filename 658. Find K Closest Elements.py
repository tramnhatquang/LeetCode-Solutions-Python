class Solution:
	class Solution:
		def findClosestElements_optimal(self, arr: List[int], k: int, x: int) -> List[int]:
			"""
			- So the main idea of it is to find out the lower bound of that k length range. The numbers between "left" and "right" are the candidates of the lower bound.
			- The if condition "x - A[mid] > A[mid + k] - x" is used to compare A[mid] and A[mid+k], see which is closer to x.
			- If A[mid] is closer to x, then A[mid+k] can never be in the k length range. So we can confidently remove all (A[mid+1], A[mid+2], A[mid+3]...) from the candidates list by set right=mid.
			- If A[mid+k] is closer to x, then A[mid] can never be in the k length range. So we can confidently remove all (...A[mid-2], A[mid-1], A[mid]) from the candidates list by set left=mid+1.
			- Once we remain only one candidate, that is left==right, we got our final lower bound.
			"""
			# Initialize binary search bounds
			left = 0
			right = len(arr) - k
			# since we only need to consider [left, right] as the lower bound range of k numbers
			res = -1
			# Binary search against the criteria described
			while left <= right:
				mid = (left + right) // 2
				if mid + k < len(arr) and x - arr[mid] > arr[mid + k] - x:
					left = mid + 1
				else:
					res = mid
					right = mid - 1

			return arr[res:res + k]

	# time: O(log(N - k) + k), N is length of arr, k is given
	# space: O(1)

	def findClosestElements_sorting(self, arr: List[int], k: int, x: int) -> List[int]:
		"""
		The brute force solution:
			- Using a custom sort based on the abs(num - x) for each number in the arr
		"""

		# sort using custom comparator
		sorted_arr = sorted(arr, key=lambda num: abs(num - x))

		# only take k elements:
		res = []
		for i in range(k):
			res.append(sorted_arr[i])

		# sort again to have output in ascending order
		return sorted(res)

# time: O(n log n + k log k)
# 1. O(n log n) for the first sort
# 2. O(k log k) for the second sort
