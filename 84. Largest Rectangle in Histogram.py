class Solution:
    def largestRectangleArea_optimal(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

    # time = space = O(n), n is length of heights

    def largestRectangleArea_brute_force(self, heights: List[int]) -> int:
        """
        Brute force solution is to find all the areas forming by any possible pairs of bars. Then, find the max area among them

        Notice that the height of a rectangle is limited by the shortest bar lying between them

        """
        # brute force solution
        max_area = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))

        return max_area
        # time: O(n^2), n is length of array
        # space: O(1)
