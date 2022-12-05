def find_product(lst):
	# Write your code here
	# left_prod = len(lst) * [1]
	# right_prod = len(lst) * [1]
	# res = len(lst) * [1]

	# example
	# [3, 4, 5, 6]
	# left = [1, 3, 12, 60]
	# right = [120, 30, 6, 1]
	# res = [120, 90, 72, 60]

	# for i in range(1, len(lst)):
	#     left_prod[i] = lst[i-1] * left_prod[i-1]

	# for i in range(len(lst) - 2, -1, -1):
	#     right_prod[i] = lst[i+1] * right_prod[i+1]

	# for i in range(len(lst)):
	#     res[i] = left_prod[i] * right_prod[i]

	# return res
	# time: O(n) = space, n : the length of arr

	# avoid using three arrays, reduce to only one arr
	res = [None] * len(lst)
	prefix = 1
	for i in range(len(lst)):
		res[i] = prefix
		prefix *= res[i]

	postfix = 1
	for i in range(len(lst) - 1, -1, -1):
		res[i] *= postfix
		postfix *= res[i]

	return res

# ex: [3, 4, 5, 6]
# [1, 3, 12, 60]
if __name__ == '__main__':
	a = b = 12
	b = 100
	c = b
	c = 1000
	print(a)
	print(b)






