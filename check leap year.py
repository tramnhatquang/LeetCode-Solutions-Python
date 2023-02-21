from pickle import FALSE
from typing import *
import math 

# Return the remainder of x/y
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
# print(math.fmod(0, 0))


def isleap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def isleap_my_implementation(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


test_cases = [(1992, True),
            (2000, True),
            (1900, False),
            (2400, True),
            (1791, False)]

for input, expected_res in test_cases:
    # print(f'input: {input}, expected res: {expected_res}')
    assert isleap(input) is expected_res
    assert isleap_my_implementation(input) is expected_res