class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        
        max_consecutive_floors = 0
        
        # Calculate the gap before the first special floor
        # Floors are from 'bottom' to 'special[0] - 1'
        # Number of floors = (special[0] - 1) - bottom + 1 = special[0] - bottom
        max_consecutive_floors = max(max_consecutive_floors, special[0] - bottom)
        
        # Calculate gaps between consecutive special floors
        for i in range(len(special) - 1):
            # Floors are from 'special[i] + 1' to 'special[i+1] - 1'
            # Number of floors = (special[i+1] - 1) - (special[i] + 1) + 1
            # = special[i+1] - special[i] - 1
            max_consecutive_floors = max(max_consecutive_floors, special[i+1] - special[i] - 1)
            
        # Calculate the gap after the last special floor
        # Floors are from 'special[-1] + 1' to 'top'
        # Number of floors = top - (special[-1] + 1) + 1 = top - special[-1]
        max_consecutive_floors = max(max_consecutive_floors, top - special[-1])
        
        return max_consecutive_floors