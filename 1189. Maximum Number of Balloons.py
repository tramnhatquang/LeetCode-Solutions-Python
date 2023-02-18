from ast import main


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        - This is a famous problem to solve what is called "bottleneck ressource"
        - Since we only care about the freq of 'b', 'a', 'l', 'o', 'n', we only need to count the freq of each char in text string
        - For the word 'balloon', we need to have 2 'l' and 2 'o' to form an instance. Find the potential of each of the five characters in isolation and then find the bottleneck character among them. 

        """
        b_count = a_count = l_count = o_count = n_count = 0
        for char in text:
            if char == 'b':
                b_count += 1
            elif char == 'a':
                a_count += 1
            elif char == 'l':
                l_count += 1
            elif char == 'o':
                o_count += 1
            elif char == 'n':
                n_count += 1

        # since we need 2 'l' and 2 'o' for each instance of 'balloon'
        l_count //= 2
        o_count //= 2
        return min(l_count, o_count, b_count, a_count, n_count)

        # time: O(n), n is length of string
        # space: O(1)

    # For a generalize solution using an array (if the word is not guranteed to be 'balloon')
    #  The potential of each character is eqaul to the number of instances in text divided by the number of instances in pattern. So we just need to find the frequqency of all the letters in ther strings text and pattern

    def find_max_number_of_pattern(self, text: str, pattern: str) -> int:
        """Algo:
            1. Store the frequency of all the characters in text in freqInText, and the frequncy of all characters in pattern in freqInPattern
            2. Find all the potential of all the lowercase English letters. The potential willm  be equal to its frequency in text divided by its frequency in pattern
            3. Return the min potential of a character
        """
        text_len = len(text)
        pattern_len = len(pattern)
        ans = float('inf')
        freq_in_text = [0] * 26  # only deal with 26 lowercase letters
        freq_in_pattern = [0] * 26

        # frequency of chracters in text
        for char in text:
            freq_in_text[ord(char) - ord('a')] += 1

        # frequency of characters in pattern
        for char in pattern:
            freq_in_pattern[ord(char) - ord('a')] += 1

        # Compare the maximum string that can be produced considering one character at a time
        for i in range(26):
            # do not divide by 0
            if freq_in_pattern[i] > 0:
                ans = min(ans, freq_in_text[i] / freq_in_pattern[i])

        return ans


s = Solution()
assert s.find_max_number_of_pattern('loonbalxballpoon', 'balloon') == 2
