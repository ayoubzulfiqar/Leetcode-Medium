class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum_val = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map_keys = {}

    def insert(self, key: str, val: int) -> None:
        old_val = self.map_keys.get(key, 0)
        delta = val - old_val
        self.map_keys[key] = val

        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.sum_val += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.sum_val