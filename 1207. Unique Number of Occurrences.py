from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        value_lst = []
        for key, value in Counter(arr).items():
            value_lst.append(value)

        if len(set(value_lst)) == len(value_lst):
            return True
        else:
            return False
