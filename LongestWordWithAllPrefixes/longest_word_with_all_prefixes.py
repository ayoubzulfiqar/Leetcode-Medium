class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def longestWord(words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = ""

    def dfs(current_node, current_path_word):
        nonlocal result

        for char in sorted(current_node.children.keys()):
            child_node = current_node.children[char]
            if child_node.is_end_of_word:
                new_word = current_path_word + char
                
                if len(new_word) > len(result):
                    result = new_word
                elif len(new_word) == len(result) and new_word < result:
                    result = new_word
                
                dfs(child_node, new_word)

    dfs(trie.root, "")

    return result