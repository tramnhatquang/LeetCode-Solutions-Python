arr = [1, 2, 3]

# print(arr)

# can be used as a stack
arr.append(4)  # O(1)
arr.append(5)  # O(1)
# print(arr)

arr.pop()  # O(1)
# print(arr)

arr.insert(1, 7)
# print(arr)  # time: O(n)

# update based on index in arr
arr[0] = 1000
arr[3] = 1001
# print(arr)

# to get the last value
arr = [4, 5, 6]
# print(arr[-1])  # 6

# indexing -2 is the second to last value, etc
# print(arr[-2])  # 5

# sliding arr
arr = [1, 2, 3, 4]
print(arr[1:3])  # [2, 3]
