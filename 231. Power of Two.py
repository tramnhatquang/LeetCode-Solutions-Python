class Solution:
    def isPowerOfTwo_approach_1(self, n: int) -> bool:
        """
        Notice that binary representation of a power of 2 are below
            1 (base 10) : 1 (base 2)
            2 (base 10) : 10 (base 2)
            4 (base 10) : 100 (base 2)
            8 (base 10) : 1000 (base 2)
        Notice that a number which is not a power of two, has more than one 1-bit in its binary representation
            3 (base 10) : 11 (base 2)
            5 (base 10) : 101 (base 2)
            6 (base 10) : 110 (base 2)
            7 (base 10) : 111 (base 2)
        Two's complement: -x = ~x + 1
        when we take x & (-x) -> keeps the right most 1 bit and set all other bits to 0.

        Conclusion: all power of twos in binary representation (x) do &( -x) get (x) back
        """
        if n <= 0:
            return False
        return n & (-n) == n
        # time = space = O(1)

    def isPowerOfTwo_approach_2(self, n: int) -> bool:
        # Turn of the rightmost 1-bit
        if n <= 0:
            return False
        return n & (n - 1) == 0
        # time = O(1) = space

    def isPowerOfTwo_brute_force(self, n: int) -> bool:
        """
        n is a power of two when n == 2^x , x>= 0 (x is a non-negative number)

        Observations:
            - n <= 0: False
            - n == 1: True
            - Check if n % 2 == 0, n //= 2. DO it until n is odd. Check if n == 1
        """
        # sanity check
        if n <= 0:
            return False

        # if we use a while loop
        while n % 2 == 0:
            n //= 2
        return n == 1

        # time: O(log n)
        # space: O(1)


print(5 & (-5))
print(4 & (-4))
print(128 & (-128))
