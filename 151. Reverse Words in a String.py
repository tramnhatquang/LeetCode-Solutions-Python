class Solution:
    # class Solution:
    def reverseWords(self, s: str) -> str:
        # def reverse_words(s: str) -> str:
        # Convert string to list of characters
        s = list(s)
        n = len(s)
        
        # Reverse the entire list of characters using two pointers
        i, j = 0, n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        # Reverse each individual word in the reversed list
        i = 0
        while i < n:
            # Skip spaces at the beginning of each word
            while i < n and s[i] == ' ':
                i += 1
            
            # Find the end of the current word
            j = i
            while j < n and s[j] != ' ':
                j += 1
            
            # Reverse the current word using two pointers
            k, l = i, j - 1
            while k < l:
                s[k], s[l] = s[l], s[k]
                k += 1
                l -= 1
            
            # Move to the next word
            i = j
        
        # Convert list of characters back to string and remove leading/trailing spaces
        s = ''.join(s).strip()
        
        # Remove extra spaces between words
        return ' '.join(s.split())

    
    
    
    def reverseWords_built_in(self, s: str) -> str:
        # split the words by space and reverse the order of the words
        list_word = s.split()[::-1] 
        return ' '.join(list_word)  
        
        # time: O(n) = space, n is length of string
        
        
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
a.reverse()
b.reverse()
print(f'{a}, {b}')