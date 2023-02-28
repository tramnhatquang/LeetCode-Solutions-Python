from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n) since we go through the string of length N two times
        # Space: O(1) because English alphabet contains 26 letters
        counter = Counter(s)
        for index, char in enumerate(s):
            if counter[char] == 1:
                return index
        return -1
