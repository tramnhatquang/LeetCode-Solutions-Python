class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = res = 0
        # count denotes the balance of the string, add 1 if curr char == (, other wise -1
        # res denotes the min open '(' to add make count balance 
        for char in s:
            if char == '(':
                bal += 1
            else:
                bal -= 1
            # 
            if bal == -1:
                bal += 1
                res += 1
        return bal + res

    def minAddToMakeValid_not_space_optimal(self, s: str) -> int:
        """
        Use a stack to solve this problem
            - Traverse thr each cahr in the string
                + if char == '(': push it to the seck
                + if char== ')':
                    * if stack is empty: count += 1 (count is the number of close parenthesis)
                    * if stack is not empty: pop() the top of the stack
            - Min number of moves required to make s valid = len(stack) + count
        """
        close_count = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append('(')
            else:
                if not stack:
                    close_count += 1
                else: # stack has at least one element, pop the top
                    stack.pop()
        return len(stack) + close_count
        # time: O(n) = space, in the worse case when we have '(((((((', stack contains up to n chars where n is length of string
    
        