class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Reapeated subtraction
        # handle the case when either dividend or divior is negative

        """
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # check an edge case
        # the case when dividend = -2147483648, divior = -1 -> return out of bound of 32-bit integers
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if dividend == 0:
            return 0

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0
        while abs_dividend >= abs_divisor:
            quotient += 1
            abs_dividend -= abs_divisor

        # if either dividend or divisior < 0
        if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend >= 0):
            quotient = -quotient
        return quotient

        # time: O(n), in the worst case secnario when divisor = 1
        # space: O(1)
