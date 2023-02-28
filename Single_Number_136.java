class Solution {
    public int singleNumberOptimal(int[] nums) {
        int res = 0;
        for (int num: nums) {
            res ^= num;
        }
        return res;
    }

    // time: O(n), n is length of nums
    // spacE: O(1)

    public int singleNumberHashMap(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int num: nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        for (int num: nums) {
            if (freq.get(num) == 1)
                return num;
        }
        return 0;
        // time: O(n) = space, n is length of nums
    }
}