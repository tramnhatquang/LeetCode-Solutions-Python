class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Brute force solution: 
            - Maintain a set of all numbers from nums arr
            - Loop over each number from 1 to n, and check if the current number is in the set. Otherwise, if it is not, append the curr number into a result arr
            - TC: O(n) = space, n is length of nums
        """
        num_set = set(nums)
        res = []
        
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                res.append(i)
                
        return res
    # time: O(n)
    # space: O(n)