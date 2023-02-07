class MedianFinder:
	"""The brute force solution is to add each number for each iteration. Then, sort the whole array and return the median.
		It takes addNum() method O(n log n) time and O(n) space.
		It takes findMedian() method O(1) = space
		This approach is not optimal, so we have to find a different way

	"""
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()


    def findMedian(self) -> float:
        n = len(self.arr)
        # if n is odd
        if n % 2 == 1: # return the middle number
            return self.arr[n // 2]
        else: # return the mean of two middle numbers
            total = self.arr[n // 2] + self.arr[n // 2 - 1]
            return total / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()