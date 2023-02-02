class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # a trie and we assume its value is empty

    def addWord(self, word: str) -> None:
        # add the given word into the trie
        curr = self.root
        for char in word:
            if char not in curr.children:
                # the current char is not in the curr node's children
                # create a new node
                newNode = TrieNode()
                curr.children[char] = newNode
                curr = newNode
            else:
                # if it is in the curr's children, me move to the children node and check the next char
                curr = curr.children[char]

        # marks that we are at the end of trie
        curr.isEndOfWord = True

        # time = space = O(n), n is length of word

    def search(self, word: str) -> bool:
        """Search the given word in the trie
        """
        # notice that if the string does not contain . operator, we just implement a basic Trie search. However, if we meet a char == '.', we have to check evey children nodes of the current node

        def dfs(index: int, root: TrieNode) -> bool:
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    # use backtracking to check every child of the curr node
                    for child in curr.children.values():
                        if dfs(index + 1, child):
                            return True
                        return False
                else:
                    if c not in curr.children:
                        return False
                    # otherwise, we move on to the next children to check for the next char
                    curr = curr.children[c]

            return curr.isEndOfWord
        return dfs(0, self.root)
        # time: O(N*26^M) where M is length of word. Since in the worst case scenario, we have something like '........z' and N is number of keys

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
