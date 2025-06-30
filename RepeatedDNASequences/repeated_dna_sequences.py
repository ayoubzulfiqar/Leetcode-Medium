import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        counts = collections.defaultdict(int)
        
        for i in range(len(s) - 9):
            substring = s[i : i + 10]
            counts[substring] += 1
        
        repeated_sequences = []
        for seq, count in counts.items():
            if count > 1:
                repeated_sequences.append(seq)
                
        return repeated_sequences