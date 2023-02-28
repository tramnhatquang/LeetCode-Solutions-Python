class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """The better solution could be only the KMP algorithm whicvh gives us O(n + m) TC, and O(n) space. However, Note: Although KMP is fast, still built-in functions of many programming languages use Brute Force. KMP is based on assumption that there would be many duplicate similar substrings. In real-world strings, this is not the case. So, KMP is not used in real-world applications. Moreover, it requires linear space.

However, it has its application in DNA sequencing. DNA is a long string of characters (A, C, G, T). There are many similar substrings in DNA. So, KMP is used in DNA sequencing.
        """
        # Brute force solution
        # 1. check every substring in the haystack and if we can get a match of a needle
        # 2. If we find our match, return the starting index. 
        # 3. After the loop ends, return -1 if there is no match
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
            
        return -1
    
        # time: O(mn) where m: length of haystack, n: length of needle
        # space: O(n) length of needle from the substring