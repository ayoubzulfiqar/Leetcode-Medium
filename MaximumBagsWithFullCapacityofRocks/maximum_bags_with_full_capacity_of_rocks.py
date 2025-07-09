class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        n = len(capacity)
        
        remaining_capacities = []
        for i in range(n):
            remaining_capacities.append(capacity[i] - rocks[i])
            
        remaining_capacities.sort()
        
        full_bags_count = 0
        
        for diff in remaining_capacities:
            if additionalRocks >= diff:
                additionalRocks -= diff
                full_bags_count += 1
            else:
                break
                
        return full_bags_count