class Solution:
    
    # optimal solutiion
    
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        In this code, we use the formula (i + 1) * (n - i) to calculate the number of times each element appears in subarrays. The expression ((i + 1) * (n - i) + 1) // 2 calculates the number of odd-length subarrays that include the element at index i. We add the product of this expression and arr[i] to the running total.

Here's an example of how to use this optimized function:
        """
        total = 0
        n = len(arr)
        for i in range(n):
            total += ((i + 1) * (n - i) + 1) // 2 * arr[i]
        return total

        # time: O(n), space: O(1)
    def sumOddLengthSubarrays_better_brute_force(self, arr: List[int]) -> int:
        """
        This way we optimize the brute force solution a little bit
        We use a sliding window, whenever the sliding window is odd-length, we append the curr_sum to ans. Then move to the next right element, by adding its value to the curr_sum so far
        """
        n = len(arr)
        total = 0
        for left in range(n):
            curr_sum = 0
            for right in range(left, n):
                curr_sum += arr[right]
                if (right - left + 1) & 1: # odd-length:
                    total += curr_sum
        return total    
        # time: O(n^2)
        # space: O(1)

    
    def sumOddLengthSubarrays_brute_force(self, arr: List[int]) -> int:
        """
        Brute force solution: Try all possible subarrays and find total sum of odd-length subarrays -> TC: O(n^3), space: O(1)
        There are 3 nested loops 
        """
        total = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                if len(arr[i:j]) & 1: # check odd-length
                    total += sum(arr[i:j])
        return total