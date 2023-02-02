class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    # if we traverse all the root-to-leaf paths, we will have distinct string words
    # each node represents a character in a string
    def __init__(self):
        self.root = TrieNode()  # root is always an empty string

    def insert(self, word: str) -> None:
        """Insert a word into the Trie
        """
        curr = self.root
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for c in word:
            if c not in curr.children:
                # If a character is not found,
                # create a new node in the trie
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True
        # time = space = O(n), n is length of word

    def search(self, word: str) -> bool:
        """Search a word in the trie
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEndOfWord
        # time = O(n), n is the length of word
        # space: O(1)

    def startsWith(self, prefix: str) -> bool:
        """Find if there is any words satrting with a given prefix
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        # time = O(n), n is the length of word
        # space: O(1)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
