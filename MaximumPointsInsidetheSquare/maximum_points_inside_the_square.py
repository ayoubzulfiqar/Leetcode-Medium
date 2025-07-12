import math

class Solution:
    def maximumPoints(self, points: list[list[int]], s: str) -> int:
        def check(r_val: int) -> bool:
            seen_tags = set()
            for i in range(len(points)):
                x, y = points[i]
                if max(abs(x), abs(y)) <= r_val:
                    tag = s[i]
                    if tag in seen_tags:
                        return False
                    seen_tags.add(tag)
            return True

        low = 0
        high = 10**9
        max_r_found = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                max_r_found = mid
                low = mid + 1
            else:
                high = mid - 1
        
        count = 0
        for i in range(len(points)):
            x, y = points[i]
            if max(abs(x), abs(y)) <= max_r_found:
                count += 1
        
        return count