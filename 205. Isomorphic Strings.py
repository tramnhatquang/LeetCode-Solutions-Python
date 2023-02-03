class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(n):
            if s[i] in map_s_to_t and map_s_to_t[s[i]] != t[i]:
                return False
            if t[i] in map_t_to_s and map_t_to_s[t[i]] != s[i]:
                return False
            map_s_to_t[s[i]] = t[i]
            map_t_to_s[t[i]] = s[i]

        return True

        # time: O(n) where n is the length of s (length of s == length of t)
        # space: O(2n) = O(n)

