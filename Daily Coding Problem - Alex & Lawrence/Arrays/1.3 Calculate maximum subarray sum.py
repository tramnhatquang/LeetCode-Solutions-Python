def maxSubArray(self, nums: List[int]) -> int:
	# use Kadane's algo
	# Initialize our variables using the first element.
	current_subarray = max_subarray = nums[0]

	# Start with the 2nd element since we already used the first one.
	for num in nums[1:]:
		# If current_subarray is negative, throw it away. Otherwise, keep adding to it.
		current_subarray = max(num, current_subarray + num)
		max_subarray = max(max_subarray, current_subarray)

	return max_subarray


# time: O(n), space: O(1)


# try every possible subarray and record the max sum of subarrays so far
# curr_max = 0
# for i in range


if __name__ == '__main__':
	arr = [1, 2, 3, 4]
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			print(arr[i:j])
