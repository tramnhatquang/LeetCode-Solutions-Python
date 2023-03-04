class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		"""
		We can solve this problem using a stack. We iterate through the asteroids from left to right, and for each asteroid, we perform the following steps:
		1. If the asteroid is moving to the right (i.e., positive), we simply append it to the stack since it cannot collide with any previous asteroid.
		2. If the asteroid is moving to the left (i.e., negative), we need to compare it with the top of the stack to see if they will collide. We keep popping elements from the stack until one of the following conditions is met:
		- The stack is empty, in which case the current asteroid survives since there is no asteroid to collide with.
		- The top of the stack is negative, in which case the current asteroid survives since it is moving to the left and cannot collide with any previous asteroid.
		- The top of the stack is positive and has a larger size than the current asteroid, in which case the current asteroid is destroyed since it is smaller and moving to the left.
		- The top of the stack is positive and has a smaller or equal size than the current asteroid, in which case both asteroids are destroyed since they have the same size or the current asteroid is larger and destroys the previous asteroid.
		3. After all the asteroids have been processed, the stack will contain the surviving asteroids. We can return the stack as the final result
		"""
		stack = []
		for asteroid in asteroids:
			if asteroid > 0:
				stack.append(asteroid)
			else:  # when we have a negative asteroid
				while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
					stack.pop()
				if not stack or stack[-1] < 0:
					stack.append(asteroid)
				elif stack[-1] == abs(asteroid):
					stack.pop()

		return stack
# time: O(n) = space, n is length of arr
