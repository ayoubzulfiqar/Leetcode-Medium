class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        n = len(s)
        prefix_parity = [0] * (n + 1)

        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            prefix_parity[i+1] = prefix_parity[i] ^ (1 << char_idx)
        
        results = []
        for left, right, k in queries:
            current_mask = prefix_parity[right+1] ^ prefix_parity[left]
            
            odd_counts = bin(current_mask).count('1')
            
            needed_changes = odd_counts // 2
            
            if needed_changes <= k:
                results.append(True)
            else:
                results.append(False)
                
        return results