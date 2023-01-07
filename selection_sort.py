def selection_sort(arr: List[int]) -> List[int] | None:
	if not arr:
		return None

	for i in range(len(arr)):
		min_index = i
		for j in range(i + 1, len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j

		# swap
		arr[min_index], arr[i] = arr[i], arr[min_index]

	return arr
