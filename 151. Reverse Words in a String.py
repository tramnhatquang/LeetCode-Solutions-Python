class Solution:
    
        
    
    def reverseWords_approach_1(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))
    # time = space = O(n)
