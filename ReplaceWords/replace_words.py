class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def get_shortest_root(self, word: str) -> str:
        node = self.root
        current_prefix_chars = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            current_prefix_chars.append(char)
            if node.is_end_of_word:
                return "".join(current_prefix_chars)
        return word

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        words = sentence.split(" ")
        replaced_words = []
        for word in words:
            replaced_words.append(trie.get_shortest_root(word))

        return " ".join(replaced_words)