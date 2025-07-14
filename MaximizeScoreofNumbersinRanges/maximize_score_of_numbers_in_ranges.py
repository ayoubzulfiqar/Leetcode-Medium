class Solution:
    def maximizeScore(self, start: list[int], d: int) -> int:
        intervals = []
        for i in range(len(start)):
            intervals.append((start[i], start[i] + d))
        
        intervals.sort()
        
        n = len(intervals)

        def check(score: int) -> bool:
            prev_chosen_val = -float('inf') 
            
            for i in range(n):
                L_i, R_i = intervals[i]
                
                current_x = max(L_i, prev_chosen_val + score)
                
                if current_x > R_i:
                    return False
                
                prev_chosen_val = current_x
                
            return True

        low = 0
        high = 2 * 10**9 + 7 
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans