def solution(arr):
	ans = 0
	for num in arr:
		ans ^= num

	return ans


if __name__ == '__main__':
	assert solution([2, 2, 1]) == 1
	assert solution([4, 1, 2, 1, 2]) == 4
