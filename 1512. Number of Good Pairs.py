class Solution:

    def numIdenticalPairs_optimal(self, nums: List[int]) -> int:
        """
        Use a hash map to optimize the time complexity

            - ex: [1, 1, 1, 1], how many pairs can we make? (6 pairs) 
            - There is 4 + 3 + 2 +1 = 4 * (3) / 2 = 6 pairs
            - The general solution is n * (n - 1) / 2
        """
        count = 0
        counter = collections.Counter(nums)
        for num, freq in counter.items():
            count += freq * (freq - 1) // 2
        return count

        # time = space = O(n)

    def numIdenticalPairs_not_optimal(self, nums: List[int]) -> int:
        """
        Brute force solution:
            - Try all possbile pairs and check if two numbers are the same, then increase the count
        """

        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count

        # time: O(n^2), space: O(1), not time optimal
