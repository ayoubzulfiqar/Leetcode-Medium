class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(capacity: int) -> bool:
            current_days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight <= capacity:
                    current_weight += weight
                else:
                    current_days += 1
                    current_weight = weight
            return current_days <= days

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans