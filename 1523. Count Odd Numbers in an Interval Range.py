class Solution:
    
    def countOdds(self, low: int, high: int) -> int:
        """
        Observation: 
            - If the range (high -low + 1) is even, the number of odd = the number of even
            - If the range(high - low + 1) is odd, the solution depends on teh parity of low and high
            - If low is odd, then for a larger integer high, the number of odd is (high - low) / 2 + 1 

        """
        # check if low is even, increment to odd
        if low % 2 == 0:
            low += 1
        
        # after incrementing, if low > high then return 0. Otherwise, return (high - low) / 2 +1 
        return 0 if low > high else (high - low) // 2 + 1
        
        # time: O(1), space: O(1)
    
    
    def countOdds(self, low: int, high: int) -> int:
        """
        Brute force sol
        """
        count = 0
        for i in range(low, high + 1):
            if i % 2: # count
                count += 1
        return count
        # time: O(high - low) = O(n), n is the diff = high - low
        # space: O(1) -> TLE
