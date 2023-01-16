class Solution:
	def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
		# use a hash map to keep track number and its index in nums2
		# loop over each number in num1 and record its index in a res arr

		res = []
		map = {}
		for index, num in enumerate(nums2):
			map[num] = index

		for num in nums1:
			res.append(map[num])

		return res

		# time: O(n) = space, since both strings have the same length
