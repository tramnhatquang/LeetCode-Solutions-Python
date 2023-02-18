class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Instead of using stack, we can think of using a 'balance'to know the number of balanced valid parentheses string. 
        Initialize a list to append all the valid characters
        1.  - We travere thr each char in s. If we meet a '(', we increase the count by 1 (count += 1)
            - If we meet a ')' parenthesis, we check If
                + count == 0, that means there are no extra open parentheses to match, that means the curr close parenthesis is invalid, so we continue the next iteration without taking the curr char
                + if count > 0, we decrease count by 1, and append the curr close parenthesis
        """
        open_count = 0
        balance = 0
        first_pass = []
        for index in range(len(s)):
            if s[index] == '(':
                open_count += 1
                balance += 1
            elif s[index] == ')':
                if balance == 0:
                    continue
                balance -= 1
            first_pass.append(s[index])
        print(f'Res arr: {first_pass}')

        res = []
        open_to_keep = open_count - balance
        for index in range(len(first_pass)):
            if first_pass[index] == '(':
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            res.append(first_pass[index])
        return ''.join(res)
    # this aprroach is helpful in term of not using the stack
    # time: O(n), n is length of s,
    # space: O(n)

    def minRemoveToMakeValid_using_stacK(self, s: str) -> str:
        """
            1. Using a stack to keep all the open parenthesis
            2. Convert all characters in s into a list of chars called list_chars
            3. Traverse thr each char in the list_chars
                - If char == '(': append its index to the stack
                - If char == ')':
                    + check if we have '(' to match since they form a valid parenthesis string, else, update list_chars[index] = '' since we have to remove it to make the string valid
            4. After the traversal, if we have left '(' parentheses in the stack, we will pop each index and update the corresponding index into an empty string in the stack

        """
        stack = []
        n = len(s)
        list_chars = list(s)
        for index in range(n):
            if s[index] == '(':
                stack.append(index)
            elif s[index] == ')':
                if stack:
                    stack.pop()
                else:
                    # remove by updating the corresponding index to an empty string
                    list_chars[index] = ''

        # check if we have left open parentheses
        while stack:
            list_chars[stack.pop()] = ''

        return ''.join(list_chars)
        # time: O(n), n is length of string
        # space: O(n) for converting a string to a list. O(n) for stack space since it can contain up to n chars. Total space complexity: O(n)
