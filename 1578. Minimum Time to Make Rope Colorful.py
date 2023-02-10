class Solution:

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # totalTime: total time needed to make rope colorful;
        # currMaxTime: maximum time of a balloon needed in this group.
        total_time = 0
        curr_max_time = 0

        # For each balloon in the array:
        for i in range(len(colors)):
            # If this balloon is the first balloon of a new group
            # set the curr_max_time as 0.
            if i > 0 and colors[i] != colors[i - 1]:
                curr_max_time = 0

            # Increment total_time by the smaller one.
            # Update curr_max_time as the larger one.
            total_time += min(curr_max_time, neededTime[i])
            curr_max_time = max(curr_max_time, neededTime[i])

        # Return total_time as the minimum removal time.
        return total_time

    def minCost_approach_1(self, colors: str, neededTime: List[int]) -> int:
        """
        If We can mutate the neededTime arr, then we can compare index i and its next consecutive (i + 1), since we want to mminimize time to remove, we want to remove the balloon who has smaller removal time
        - If the removal time of i > removal time of i + 1, we can update the removal time of (i + 1) = removal time of i and continue comparing for the next iteration 

        """
        n = len(colors)
        min_removal_time = 0
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                if neededTime[i] <= neededTime[i + 1]:
                    min_removal_time += neededTime[i]
                else:
                    # update removal time of (i + 1) = removal time of i for the next iteration
                    min_removal_time += neededTime[i + 1]
                    neededTime[i + 1] = neededTime[i]
        return min_removal_time

        # time: O(n), space: O(1)
