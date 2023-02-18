class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Using stack to solve this problem. Whenever we append a new character into the stack, we check if the top element is different from the current char, if they are the same, we remove the top element
            - Otherwise, we keep appending the curr char into the stack
            - all characters in the stack is all remaining chars after removing all nearby duplicates
        """
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
        # time: O(n) = space