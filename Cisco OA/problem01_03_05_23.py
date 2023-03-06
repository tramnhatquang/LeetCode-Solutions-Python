"""
https://leetcode.com/discuss/interview-question/3216097/CIsco-OA-SHL-Questions
"""


def check_sorted(s: str):
	"""
	- Write an algorithm to check if a string is sorted in alphabetical order and print 0 if it is. If it is not in alphabetical order, then print the index of the character where it is out of alphabetical order

	- Input: the input consists of a string
	- Output: Print '0' if the given string is in alphabetical order, if not print the index of the character where it is out of alphabetical order
	"""
	index = -1
	for i in range(1, len(s)):
		if s[i] < s[i - 1]:
			index = i
			break
	return 0 if index == -1 else index


if __name__ == '__main__':
	print(check_sorted('abc'))  # 0
	print(check_sorted('abcd'))  # 0
	print(check_sorted('asd'))  # 2
	print(check_sorted('fbc'))  # 1
