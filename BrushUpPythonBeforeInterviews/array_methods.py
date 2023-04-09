# reverse
nums = [1, 10, 3]
nums.reverse()

print(nums)  # [3, 10, 1]

### sorting

## numbers
arr = [5, 4, 3, 2, 1]
arr.sort()
print(arr)  # [1, 2, 3, 4, 5]

## string
arr = ['bob', 'alice', 'jane', 'doe']
arr.sort()
print(arr)  # ['alice', 'bob', 'doe', 'jane']]

## custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)  # ['bob', 'doe', 'jane', 'alice']
