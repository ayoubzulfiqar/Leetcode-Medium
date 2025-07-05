import collections

class Solution:
    def minDeletions(self, s: str) -> int:
        freq_map = collections.Counter(s)
        
        # Get frequencies and sort them in descending order
        # Processing higher frequencies first gives more room to decrement
        frequencies = sorted(freq_map.values(), reverse=True)
        
        seen_frequencies = set()
        deletions = 0
        
        for freq in frequencies:
            current_freq = freq
            # While the current frequency is not unique and is greater than 0,
            # decrement it and count a deletion.
            while current_freq > 0 and current_freq in seen_frequencies:
                current_freq -= 1
                deletions += 1
            
            # If the frequency becomes 0, we don't add it to seen_frequencies
            # as characters with 0 frequency are ignored.
            if current_freq > 0:
                seen_frequencies.add(current_freq)
                
        return deletions