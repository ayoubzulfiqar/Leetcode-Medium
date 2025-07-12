class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        
        max_overall_energy = -float('inf') 
        
        for i in range(n - 1, -1, -1):
            if i + k < n:
                energy[i] += energy[i + k]
            
            max_overall_energy = max(max_overall_energy, energy[i])
            
        return max_overall_energy