class Solution:
    def combinationSum_dfs(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index: int, path: List[int], curr_sum: int) -> None:
            # base case
            if curr_sum == target:
                res.append(path)
                return
            if index >= len(candidates) or curr_sum > target:
                return

            for i in range(index, len(candidates)):
                # include the number
                dfs(i, path + [candidates[i]], curr_sum + candidates[i])

        dfs(0, [], 0)
        return res
    # time: O(n ^(T/M + 1)), n is number of candidates, T be the target value, M is the minimal value
    # space: O(T/M)

    def combinationSum_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index: int, path: List[int], curr_sum: int) -> None:
            # base case
            if curr_sum == target:
                res.append(path.copy())
                return

            if index >= len(candidates) or curr_sum > target:
                return

            path.append(candidates[index])
            # include the number
            dfs(index, path, curr_sum + candidates[index])
            path.pop()
            # do not include the number
            dfs(index + 1, path, curr_sum)

        dfs(0, [], 0)
        return res
