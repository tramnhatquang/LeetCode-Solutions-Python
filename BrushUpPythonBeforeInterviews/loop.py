# a basic while loop
i = 0
while i < 10:
	i += 1

# a basic for-loop
for i in range(10):
	print(i)  # i goes from 0 to 9 inclusively

print('\n')  # for an empty line

for i in range(1, 10):
	print(i)  # i goes from 1 to 10 inclusively

print('\n')

for i in range(1, 10, 2):
	print(i)  # i goes from 1 to 9, but only print odd numbers (1, 3, 5, 7, 9)

print('\n')

for i in range(10, 0, -1):
	print(i)  # i goes in the reversed order (from 10 to 1)
