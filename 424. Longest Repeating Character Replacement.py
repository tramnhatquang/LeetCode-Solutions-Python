import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        res = 0
        left = 0

        longest = 0
        for right in range(len(s)):
            count[s[right]] += 1
            longest = max(longest, count[s[right]])

            # check if we have a valid window
            if (right - left + 1) - longest > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
    # time: O(n), n is the length of string
    # space: O(26) = O(m), m consists of 26 lowercase letters
