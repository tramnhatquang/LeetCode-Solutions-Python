class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        - Count the freq of each number in a hash map
        - Visit each number and record the max num we see so far if its count = 1
        """
        max_num = float('-inf')
        counter = Counter(nums)
        for num, freq in counter.items():
            if freq == 1:
                max_num = max(num, max_num)
        
        return max_num if max_num != float('-inf') else -1 
        # time = space = O(n)