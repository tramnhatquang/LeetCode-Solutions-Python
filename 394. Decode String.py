class Solution:
    def decodeString(self, s: str) -> str:
        k = 0
        stack = []
        curr_str = ''
        for char in s:
            if char == '[':
                stack.append((curr_str, k))
                curr_str, k = '', 0
            elif char == ']':
                last_str, last_k = stack.pop()
                curr_str = last_str + curr_str * last_k
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                curr_str += char
        return curr_str
