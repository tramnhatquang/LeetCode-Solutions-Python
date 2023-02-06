"""Implement a function that takes an array testVariable containing opening ( and closing parenthesis ) and determines whether or not the brackets in the array are balanced. The function also takes startIndex = 0 and currentIndex = 0 as parameters.
    """


def balanced_recursive(testVariable, startIndex=0, currentIndex=0):
    if startIndex == len(testVariable):
        return currentIndex == 0

    if currentIndex < 0:
        return False

    if testVariable[startIndex] == "(":
        return balanced_recursive(testVariable, startIndex + 1, currentIndex + 1)
    elif testVariable[startIndex] == ")":
        return balanced_recursive(testVariable, startIndex + 1, currentIndex - 1)


def balanced_iterative(testVariable, startIndex=0, currentIndex=0):
    # Write your code here
    stack = []
    for char in testVariable:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            return False
    return not stack


assert balanced_iterative(['(', '(', ')', ')', '(', ')']) is True
assert balanced_iterative(['(', ')', '(', ')']) is True
assert balanced_iterative([')', '(']) is False

assert balanced_recursive(['(', '(', ')', ')', '(', ')']) is True
assert balanced_recursive(['(', ')', '(', ')']) is True
assert balanced_recursive([')', '(']) is False
