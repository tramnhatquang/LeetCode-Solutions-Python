from collections import Counter


class Solution:
    def isAnagram_normal(self, s: str, t: str) -> bool:
        # use hash maps to count the frequencies of two strings and compare them together. They are valid anagram if each char's freq is the same
        if len(s) != len(t):
            return False

        import collections
        map_s = collections.defaultdict(int)
        map_t = collections.defaultdict(int)

        # count s:
        for char in s:
            map_s[char] += 1

        # count t
        for char in t:
            map_t[char] += 1

        return map_s == map_t

    # time: O(n)

    def isAnagram_sort(self, s: str, t: str) -> bool:
        # two words are anagrams if their sorted strings are the same
        return sorted(s) == sorted(t)

    # time: O(n log n), space: O(n)
    def isAnagram_built_in_func(self, s: str, t: str) -> bool:
        # use built-in function
        return Counter(s) == Counter(t)

# time: O(n), two words must have the same length
# space: O(n)
