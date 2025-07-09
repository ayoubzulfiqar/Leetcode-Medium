class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def check(x: int) -> bool:
            stores_needed = 0
            for q in quantities:
                stores_needed += (q + x - 1) // x
            return stores_needed <= n

        low = 1
        high = max(quantities)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans