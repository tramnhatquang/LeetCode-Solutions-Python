import bisect


def smaller_counts(lst):
	result = []
	seen = []

	for num in reversed(lst):
		i = bisect.bisect_left(seen, num)
		result.append(i)
		bisect.insort(seen, num)

	return list(reversed(result))

if __name__ == '__main__':
	arr = [3, 4, 9, 6, 1]
	print(smaller_counts(arr))
