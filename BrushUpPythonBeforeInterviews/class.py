class MyClass:
	# constructor
	def __int__(self, nums):
		# create member variables
		self.nums = nums
		self.size = len(nums)

	# self key word required as param
	def getLength(self):
		return self.size

	def getDoubleLength(self):
		return 2 * self.getLength()
