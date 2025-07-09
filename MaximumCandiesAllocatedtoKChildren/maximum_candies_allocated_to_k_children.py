class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        low = 0
        high = max(candies)
        
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid == 0:
                ans = mid
                low = mid + 1
                continue

            current_piles_possible = 0
            for pile_size in candies:
                current_piles_possible += pile_size // mid

            if current_piles_possible >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans