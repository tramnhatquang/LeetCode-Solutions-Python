# division is decimal by default
print(5 / 2)  # 2.5
print(3 / 1)  # 3.0
# print(1 / 0)  # error, division by zero


# integer division
print(5 // 2)  # 2
print(10 // 2)  # 5

'''
Careful: most languages round towards 0 by default so negative numbers will round down
'''
print(-3 // 2)  # -2

'''
A workaround for rounding towards zero is to use decimal division and then convert to int
'''
print(int(-3 / 2))  # -1

# module
print(10 % 3)  # 1

# except for negative values
print(-10 % 3)  # 2

# to be consistent with other languages
import math

print(math.fmod(-10, 3))

# more math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# max number
max = float('inf')
min = float('-inf')

# Python numbers are infinite sp they never overflow
print(math.pow(2, 200))
