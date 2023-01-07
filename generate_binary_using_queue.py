from collections import deque


def find_bin(number):
	result = []
	queue = deque()
	queue.append(1)
	for i in range(number):
		result.append(str(queue.popleft()))
		s1 = result[i] + "0"
		s2 = result[i] + "1"
		queue.append(s1)
		queue.append(s2)

	return result  # For number = 3 , result = {"1","10","11"}


# print(find_bin(2))
print(find_bin(5))
# print(find_bin(10))
# print(find_bin(3))
