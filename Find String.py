

from typing import *


def find_string(str1: str, str2: str) -> int:
    """
    Returns the index of the first occurrence of str2 in str1, or -1 if not found
    """
    # brute force solution
    # try each char in str2 from left and right and check if its in the str1

    # Time: O(mn) time where m, n are len(str1) and len(str2)

    """Better approach is to use two pointers, one for str1, and one for str2.
        Algo:
        1. Initialize two pointers, one for str1, one for str2. Let's call it p1, p2


        2. Do a while loop until p1 >= len(str1) or p2 >= len(str2)
            - If str1[p1] == str2[p2], return p1
            - If str1[p1]!= str2[p2]:
                + If str1[p2] == '*', return p2
                + If str1[p2]!= '*', move p2, and p1 to the next position

    """
    s1Len, s2Len = len(str1), len(str2)
    if s2Len > s1Len:
        return -1
    
    p1 = p2 = 0
    res = -1
    while p1 < s1Len and p2 < s2Len:
        if str1[p1] == str2[p2] or str2[p2] == '*':
            p1 += 1
            p2 += 1
            res = p1 # update the first occurrence
        else:
            p1 += 1


    print(f'Res: {res}')
    return -1 if p2 !=s2Len else res



assert find_string('xabcdey', 'ab*de') == 1
assert find_string('aaaab', '*') == 0
assert find_string('abcd', '****') == 0
assert find_string('abcd', '*b*d') == 0
assert find_string('abc', 'abc') == 0
assert find_string('abc', 'defg') == -1
assert find_string('abc', 'def') == -1
assert find_string('abcdef', 'def') == 3


