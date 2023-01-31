class Solution:

    def getSum_easy_approach(self, a: int, b: int) -> int:
        while b != 0:
            # sum without carry
            sum_without_carry =  a ^ b
            # carry
            carry = (a & b ) << 1
            a = sum_without_carry
            b = carry
        return a
    # time= space = O(1)

    def getSum_cheat_approach(self, a: int, b: int) -> int:
        return a + b
        # time: O(1) = space, but not accepted since I cannot use + or - in the Solution

