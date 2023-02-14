from collections import Counter, defaultdict


class Solution:

    def checkInclusion_using_arr(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        # use two arrays to store the occurrences
        # we only deal with 26 lowercase letters
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        # find all occurrences of char in s1, stored them in s1_counter
        for char in s1:
            s1_counter[ord(char) - ord('a')] += 1

        left = 0
        for right in range(s2_len):
            # update the char in s2_counter
            curr_char = s2[right]
            s2_counter[ord(curr_char) - ord('a')] += 1

            # maintain a window length of size == s1.length
            if right - left + 1 > s1_len:
                s2_counter[ord(s2[left]) - ord('a')] -= 1
                left += 1  # move the left pointer to maintain the window length

            # we have a match permutation
            if s1_counter == s2_counter:
                return True
        return False

    def checkInclusion_using_map(self, s1: str, s2: str) -> bool:
        """
        Two string are permutation of each other if they have the same characters with the same frequencies of characters
        The brute force solution is to check every possible substrings of s2 whose length == s1 and see if there is a permutation of s1 in s2.
            - TC: O(n *m), n is s1's length, m is s2's length
            - SC: O(n * m)

        Algo:
            1. We use a Counter to count all chars and their freq in s1 string
            2. We maintain a sliding window whose length = s1.string, and it is maintained by using left and right pointers. 
            3. We traverse thr each char in the s2s tring
                - Update the curr char's freq in the window counter
                - If the window counter == s1_counter, return True
                - If the window length > s1.string, we decrement the left char freq in the window counter and move left to the right by 1
        """
        # sanity check
        if len(s1) > len(s2):
            return False

        # count the number of freq in s1 string
        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            # always maintain a sliding window length == s1.length
            if right - left + 1 > len(s1):
                s2_counter[s2[left]] -= 1
                if s2_counter[s2[left]] == 0:
                    # remove the char from counter if its freq == 0
                    del s2_counter[s2[left]]
                left += 1  # move left to maintain the window length

            s2_counter[s2[right]] += 1

            # print(f's2_counter: {s2_counter}')
            # print(f'Left: {left}')
            # print(f'Right: {right}')
            if s2_counter == s1_counter:  # check permutation
                return True

        return False
        # space: O(n + (m - n)) = O(m), m is length of s2, n is length of s1
        # space: O(n), n is length of s1, used in the s1 counter and s2 counter
