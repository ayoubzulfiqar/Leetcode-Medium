import collections

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_counts = collections.Counter(word)
        frequencies = sorted(char_counts.values(), reverse=True)
        
        total_pushes = 0
        num_keys = 8 
        
        for i, freq in enumerate(frequencies):
            push_cost = (i // num_keys) + 1
            total_pushes += freq * push_cost
            
        return total_pushes