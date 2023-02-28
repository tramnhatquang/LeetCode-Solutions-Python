class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, 0, res, new ArrayList<Integer>());
        return res;
    }

    // helper function to generate all possible subsets
    public void dfs(int[] nums, int startIndex, List<List<Integer>> res, List<Integer> subset) {
        // append the subset being constructed so far into the result
        res.add(new ArrayList<>(subset)); // create a new copy
        for (int i = startIndex; i < nums.length; i++) {
            subset.add(nums[i]);
            dfs(nums, i + 1, res, subset);
            subset.remove(subset.size() - 1);
        }

    }

    // time: O(n * 2^n), n is length of arr
    // space: O(n), how much the recursive calls take
}