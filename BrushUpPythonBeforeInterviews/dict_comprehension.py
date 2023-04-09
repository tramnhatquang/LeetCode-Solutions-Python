# Dict comprehension
myMap = {'a': 1, 'b': 2, 'c': 3}

mySecondMap = {i: 2 * i for i in range(3)}

print(f'My second map: {mySecondMap}')

# looping thr map
for key in myMap:
	print(f'Key: {key}')

for key, val in myMap.items():
	print(f'Key: {key}, value: {val}')

for val in myMap.values():
	print(f'Current value: {val}')
