def find_max_sum_sublist(lst):
	# Write your code here!
	start = end = 0
	curr_max = global_max = 0
	for index, num in enumerate(lst):
		if curr_max < 0:
			curr_max = num
			# start = index
		else:
			curr_max += num
		if global_max < curr_max:
			global_max = curr_max
			# end = index
	# print(start, end + 1)
	return global_max


if __name__ == '__main__':
    print(find_max_sum_sublist([2, -8, 4, 5]))






