from functools import lru_cache


def func(x: int) -> int:
    if x == 1:
        return 0
    if x == 2:
        return 1
    return func(x - 1) + func(x - 2)


print(func(5))
print()
