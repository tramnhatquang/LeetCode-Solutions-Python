class Solution:

	def getRow(self, rowIndex: int) -> List[int]:
		if rowIndex == 0:
			return [1]

		middle = []
		prevRow = self.getRow(rowIndex - 1)

		for i in range(len(prevRow) - 1):
			middle.append(prevRow[i] + prevRow[i + 1])

		return [1] + middle + [1]
