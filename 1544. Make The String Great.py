class Solution:
    def makeGood(self, s: str) -> str:
        """
        Two strings are same letters, but one is in upper case, the other is in lowercase or vice-versa -> let call them s[i], s[i + 1] and

            - when Math.max(ord(s[i]) - ord(s[i + 1])) == 32
            For example, a = 65, A = 97

        """
        stack = []
        for curr_char in s:
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        return ''.join(stack)

        # time  = space  = O(n)
        