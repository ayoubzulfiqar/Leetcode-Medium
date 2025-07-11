class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num_str):
        node = self.root
        for char_digit in num_str:
            if char_digit not in node.children:
                node.children[char_digit] = TrieNode()
            node = node.children[char_digit]

    def get_longest_common_prefix_length(self, num_str):
        node = self.root
        current_lcp_length = 0
        for char_digit in num_str:
            if char_digit in node.children:
                node = node.children[char_digit]
                current_lcp_length += 1
            else:
                break
        return current_lcp_length

def find_longest_common_prefix_length(arr1: list[int], arr2: list[int]) -> int:
    trie = Trie()

    for num in arr1:
        trie.insert(str(num))

    max_lcp_length = 0

    for num in arr2:
        current_num_str = str(num)
        lcp = trie.get_longest_common_prefix_length(current_num_str)
        max_lcp_length = max(max_lcp_length, lcp)

    return max_lcp_length