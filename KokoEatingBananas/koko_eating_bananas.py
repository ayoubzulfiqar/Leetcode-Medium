class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        ans = high 
        
        while low <= high:
            mid = low + (high - low) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid 
                
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans