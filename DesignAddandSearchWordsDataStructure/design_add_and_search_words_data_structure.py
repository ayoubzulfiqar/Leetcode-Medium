class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def _dfs(node, index):
            if index == len(word):
                return node.is_end_of_word

            char = word[index]

            if char == '.':
                for child_char in node.children:
                    if _dfs(node.children[child_char], index + 1):
                        return True
                return False
            else:
                if char in node.children:
                    return _dfs(node.children[char], index + 1)
                else:
                    return False

        return _dfs(self.root, 0)