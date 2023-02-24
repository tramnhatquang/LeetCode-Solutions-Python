def is_palindrome(s):
    # Write your code here
    # Tip: You may use the code template provided
    # in the two_pointers.py file
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
    