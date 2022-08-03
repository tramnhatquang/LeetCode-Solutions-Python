class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(n) where n is the length of list
        # Space: O(n)
        #         hash_table = {}

        #         for i, v in enumerate(nums):
        #             if v in hash_table and i - hash_table[v] <= k:
        #                 return True

        #             hash_table[v] = i
        #         return False

        # Using set and sliding window approach
        # Time: O(n)
        # Space optimization: O(k) where k is given
        table = set()

        for i, v in enumerate(nums):
            if v in table:
                return True
            table.add(v)
            if len(table) > k:
                table.remove(nums[i - k])
        return False
