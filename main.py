from typing import *


def minMeetingRooms(intervals: List[List[int]]) -> int:
	time = []
	for start, end in intervals:
		time.append((start, 1))
		time.append((end, -1))

	time.sort(key=lambda x: (x[0], x[1]))
	print(f'Time: {time}')
	count = 0
	max_count = 0
	for t in time:
		count += t[1]
		max_count = max(max_count, count)
	return max_count


def search_left_most(nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1
	res = -1
	while left <= right:
		mid = (left + right) // 2
		if nums[mid] < target:
			left = mid + 1
		else:
			res = mid
			right = mid - 1
	print(f'Res: {res}')
	return res


def find_longest_substring(string: str) -> int:
	stack = [-1]
	max_len = 0
	count_question_marks = 0
	for index, char in enumerate(string):
		if char == '<':
			stack.append(index)
		elif char == '?':
			count_question_marks += 1
			if stack:
				if stack[-1] == -1:
					continue
				else:
					max_len = max(max_len, index - stack[-1] + 1)
			stack.append(index)
		else:
			stack.pop()
			if not stack:
				stack.append(index)
			else:
				max_len = max(max_len, index - stack[-1])

	return max(max_len, count_question_marks)


def test_cases_longest_substring() -> None:
	test = [('<><??>>', 4),
			('??????', 6),
			('<<?', 2),
			('>?', 0),
			('<', 0),
			('??', 2),
			('<<<???', 6),
			('<<?<?>>?', 8)]
	for input, expected_answer in test:
		print(f'Curr input: {input}')
		output = find_longest_substring(input)
		print(f'Curr output: {output}\n')
		assert output == expected_answer


if __name__ == '__main__':
	test_cases_longest_substring()
# print(find_longest_substring('<><??>>'))
