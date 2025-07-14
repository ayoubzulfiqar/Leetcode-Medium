class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

class Solution:
    def minimumNumberofValidStrings(self, words: list[str], target: str) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            current_trie_node = trie.root
            for j in range(i, n):
                char = target[j]
                if char not in current_trie_node.children:
                    break
                
                current_trie_node = current_trie_node.children[char]
                dp[j+1] = min(dp[j+1], dp[i] + 1)
        
        return dp[n] if dp[n] != float('inf') else -1