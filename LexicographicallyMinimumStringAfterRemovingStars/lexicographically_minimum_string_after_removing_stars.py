import collections

class Solution:
    def solve(self, s: str) -> str:
        char_indices = [collections.deque() for _ in range(26)]
        removed_indices = set()
        
        for i, char in enumerate(s):
            if char == '*':
                for j in range(26):
                    if char_indices[j]:
                        idx_to_remove = char_indices[j].pop()
                        removed_indices.add(idx_to_remove)
                        break
            else:
                char_indices[ord(char) - ord('a')].append(i)
        
        result_chars = []
        for i, char in enumerate(s):
            if char != '*' and i not in removed_indices:
                result_chars.append(char)
                
        return "".join(result_chars)