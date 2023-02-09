class Solution:

    def lengthOfLastWord_one_pass(self, s: str) -> int:
        p, length = len(s), 0

        while p > 0:
            p -= 1
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length

        return length

    def lengthOfLastWord_two_passes(self, s: str) -> int:
        """
        Pay attention to some cases:
            - The string is empty
            - There could be some trailing spaces(i.e. " hello ")
            - There might be only one world
        """
        # trim all the trailing spaces
        n = len(s) - 1
        length = 0
        while n >= 0 and s[n] == ' ':
            n -= 1

        # count the last word
        while n >= 0 and s[n] != ' ':
            n -= 1
            length += 1

        return length

        # time: O(n), sapce: O(1)
