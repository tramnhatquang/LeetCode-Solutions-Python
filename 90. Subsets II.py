class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to handle duplicates
        nums.sort()
        # Initialize the output list with an empty subset
        res = []
        # Call the recursive function with the starting index, current subset, and output list
        self.dfs(nums, 0, [], res)
        return res
    
    # time: O(n * 2^n), n is length of nums
    # space: O(n)

    def dfs(self, nums, start, curr, res):
        # For each starting index, generate all possible subsets with and without the current element
        res.append(curr.copy())
        for i in range(start, len(nums)):
            # Skip duplicates by checking the current and previous elements
            if i > start and nums[i] == nums[i-1]:
                continue
            # Append the current element to the current subset and generate all subsets starting from the next index
            curr.append(nums[i])
            # Append the new subset to the output list
            # Generate all subsets starting from the next index
            self.dfs(nums, i + 1, curr, res)
            curr.pop()  # Backtrack to the previous subset by removing the last element
