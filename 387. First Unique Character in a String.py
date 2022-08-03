from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n) since we go through the string of length N two times
        # Space: O(1) because English alphabet contains 26 letters
        hash_table = Counter(s)
        for i in range(len(s)):
            if hash_table[s[i]] == 1:
                return i
        return -1

        # Another way without using Counter
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        for idx, char in enumerate(s):
            if dic[char] == 1:
                return idx
        return -1