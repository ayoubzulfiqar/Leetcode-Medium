class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            
            if self._can_make_bouquets(bloomDay, m, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

    def _can_make_bouquets(self, bloomDay: list[int], m: int, k: int, day_limit: int) -> bool:
        bouquets_made = 0
        current_adjacent_flowers = 0
        
        for bloom_date in bloomDay:
            if bloom_date <= day_limit:
                current_adjacent_flowers += 1
                if current_adjacent_flowers == k:
                    bouquets_made += 1
                    current_adjacent_flowers = 0
            else:
                current_adjacent_flowers = 0
            
            if bouquets_made >= m:
                return True
                
        return bouquets_made >= m