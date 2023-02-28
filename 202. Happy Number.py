class Solution:

    def isHappy_slow_fast_pointer(self, n: int) -> bool:
        # using slow and fast pointers
        def sum_digits(n: int) -> int:
            total_sum = 0
            while n:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        if n == 1:
            return True

        slow = n
        fast = sum_digits(n)
        while fast != 1 and fast != slow:
            fast = sum_digits(sum_digits(fast))
            slow = sum_digits(slow)
            # If the fast pointer ever reaches 1, we know that n is a happy number and we return True. If the slow and fast pointers become equal, we know that we are stuck in a cycle and can return False.
        return fast == 1
        # time = space = O(log n)

    def isHappy_using_set(self, n: int) -> bool:
        """
        Detect a cycle with a HashSet
        1. We keep doing the stimulation and for each new calculation we check if we already computed thta number. If a number is already in the set, we know we are in a cycle and eventually return False
        2. If the new number is 1, we return False
        """
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
        # time: O(log n) = space, n is the given number
