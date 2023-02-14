class Solution:
    
    
    
    def wordBreak_brute_force_2(self, s: str, wordDict: List[str]) -> bool:
        
        def checkWord(start: int) -> bool:
            if start == len(s): # we reach the target
                return True
            res = False # initial state, since we have not matched anything yet
            for word in set(wordDict):
                if s[start:].startswith(word):
                    res = res or checkWord(start + len(word))
            
            return res
        return checkWord(0)
    """
    Check each word in dictionary is a prefix of the original word. If there is a  match, we check the remaining part of the string if there is match to move on
    At each state of node, we have to check m words in the dictionary, the 
    """
    # time: O(m^(n/(shortest word size))) * n. where m is the number of words
    # space: O(n)
    
    def wordBreak_brute_force_1(self, s: str, wordDict: List[str]) -> bool:
        """
        Brute force solution: Try every word in dictionary of words and if it is found in the dictionmry, then recrusive function is called for the remaining portion of that string. And, if in some function call, it is found that the complete  string is in dinctionaru, then it will return True
        """
        wordDict = set(wordDict)
        def is_in_dict(s: str, start: int) -> bool:
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and is_in_dict(s, end):
                    return True
            return False
        return is_in_dict(s, 0)

    # time: O(2^n), n is length of the input string
    # space: O(n)
