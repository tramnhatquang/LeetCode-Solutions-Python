nums = [1, 2, 3]

# using index
for i in range(len(nums)):
	print(nums[i])

# without index
for n in nums:
	print(n)

# with index, value
for i, n in enumerate(nums):
	print(f'Index: {i}, number: {n}')
