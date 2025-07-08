class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counts = [0] * (1 << 10)
        counts[0] = 1
        
        total_wonderful_substrings = 0
        current_mask = 0
        
        for char_code in word:
            current_mask ^= (1 << (ord(char_code) - ord('a')))
            
            total_wonderful_substrings += counts[current_mask]
            
            for k in range(10):
                target_prev_mask = current_mask ^ (1 << k)
                total_wonderful_substrings += counts[target_prev_mask]
            
            counts[current_mask] += 1
            
        return total_wonderful_substrings