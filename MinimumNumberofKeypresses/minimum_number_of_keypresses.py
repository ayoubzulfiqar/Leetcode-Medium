import collections

class Solution:
    def minimumKeypresses(self, s: str, k: int) -> int:
        freq_map = collections.Counter(s)
        frequencies = sorted(freq_map.values(), reverse=True)
        
        total_keypresses = 0
        press_multiplier = 1
        chars_assigned_to_current_multiplier = 0
        
        for freq in frequencies:
            total_keypresses += freq * press_multiplier
            chars_assigned_to_current_multiplier += 1
            
            if chars_assigned_to_current_multiplier == k:
                press_multiplier += 1
                chars_assigned_to_current_multiplier = 0
                
        return total_keypresses