class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        def calculate_sum(val: int) -> int:
            current_sum = 0
            for x in arr:
                current_sum += min(x, val)
            return current_sum

        left = 0
        right = max(arr) 

        best_diff = float('inf')
        best_value = 0

        while left <= right:
            mid = left + (right - left) // 2
            current_sum = calculate_sum(mid)
            current_diff = abs(current_sum - target)

            if current_diff < best_diff:
                best_diff = current_diff
                best_value = mid
            elif current_diff == best_diff:
                best_value = min(best_value, mid)

            if current_sum < target:
                left = mid + 1
            elif current_sum > target:
                right = mid - 1
            else: 
                best_value = min(best_value, mid)
                right = mid - 1

        return best_value