from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        
        num_blocks = n // k
        
        block_counts = Counter()
        
        for i in range(0, n, k):
            block = word[i : i + k]
            block_counts[block] += 1
            
        max_freq = 0
        # According to constraints (1 <= n, 1 <= k), num_blocks will always be at least 1,
        # ensuring block_counts will not be empty.
        max_freq = max(block_counts.values())
        
        return num_blocks - max_freq