class Solution:
    
    def addDigits_optimal(self, num: int) -> int:
        """
        mathematical approach: DIGITAL ROOt
            - If a number == 0 -> its digital root = 0
            - IF a number is divisible by 9 -> its digital root is 9
            - Else take n module of 9
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
    
        # time = space =O(1)
    def addDigits_not_optimal(self, num: int) -> int:
        digit = 0
        while num:
            digit += num % 10
            num //= 10
            
            # updating num until num has only one digit
            if num == 0 and digit > 9:
                num = digit
                digit = 0
        return digit
    
    # time: O(log n)
    # space: O(1)