class TrieNode:
    def __init__(self):
        self.children = {}
        self.count_end = 0
        self.count_prefix = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count_prefix += 1
        curr.count_end += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count_end

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count_prefix

    def erase(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            curr.count_prefix -= 1
        curr.count_end -= 1