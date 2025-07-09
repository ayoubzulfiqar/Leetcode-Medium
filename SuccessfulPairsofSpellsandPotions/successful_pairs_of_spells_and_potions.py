import bisect

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        n = len(spells)
        
        result = [0] * n
        
        for i in range(n):
            spell_strength = spells[i]
            
            min_required_potion = success / spell_strength
            
            idx = bisect.bisect_left(potions, min_required_potion)
            
            num_successful_potions = m - idx
            
            result[i] = num_successful_potions
            
        return result