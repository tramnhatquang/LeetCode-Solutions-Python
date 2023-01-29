import copy

a = [[1, 2], 3, 4]
b = copy.deepcopy(a)  # use deepcopy
# b = a.copy() # shallow copy
# similarly to b = a[:]

print('a: ', a)
print('b: ', b)

# modifying a
a[1] = 10
print("\nAfter modifying a")
print('a: ', a)
print('b: ', b)

# modifying b
b[1] = 100
print("\nAfter modifying b")
print('a: ', a)
print('b: ', b)

# modifying the list of list in a
a[0][1] = 50
print("\nAfter modifying list of list in a")
print('a: ', a)
print('b: ', b)
