class Solution:

	def isRobotBounded_easy_understanding(self, instructions: str) -> bool:
		d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
		x, y = 0, 0
		index = 0
		for i in instructions:
			if i == 'L':
				index = (index + 3) % 4
			elif i == 'R':
				index = (index + 1) % 4
			else:
				x += d[index][0]
				y += d[index][1]
		return (x, y) == (0, 0) or index != 0

	def isRobotBounded_pythonic(self, instructions: str) -> bool:
		# the observation is that after one sequence of instructions,
		#   1. if chopper return to the origin, he is obvious in an circle.
		#   2. if chopper finishes with face not towards north,it will get back to the initial status in another one or three sequences.
		x, y, dx, dy = 0, 0, 0, 1

		# set dx = 0, dy = 1 since the robot starts facing north in the begining
		for instruction in instructions:
			if instruction == 'G':
				x += dx
				y += dy
			elif instruction == 'L':
				dx, dy = -dy, dx
			else:  # instruction == 'R'
				dx, dy = dy, -dx
		return (x, y) == (0, 0) or (dx, dy) != (0, 1)

# tiem: O(n), dx, dy represent the direction
# space: O(1),
