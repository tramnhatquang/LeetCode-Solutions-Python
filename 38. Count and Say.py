class Solution:
    def countAndSay(self, n: int) -> str:
        curr_string = '1'
        for _ in range(n - 1):
            next_string = ''
            i = 0
            while i < len(curr_string):
                count = 1
                while i + 1 < len(curr_string) and curr_string[i] == curr_string[i + 1]:
                    i += 1
                    count += 1
                next_string += str(count) + str(curr_string[i])
                i += 1
            # update curr_stringn
            curr_string = next_string
        return curr_string
        # time = space = O(4^n/3)