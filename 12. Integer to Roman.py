class Solution:
    def intToRoman(self, num: int) -> str:
        # Time: O(1) because we have a finite set of roman numericals.
        # Space: O(1). the amount of memory used does not change with the size of the input integer, and is therefore constant
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        res = ''
        for value, symbol in dic.items():
            if num == 0: break
            count, num = divmod(num, value)
            res += symbol * count
        return res