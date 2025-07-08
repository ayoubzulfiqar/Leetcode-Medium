class Solution:
    def minimumLimit(self, nums: list[int], maxOperations: int) -> int:
        def check(P: int) -> bool:
            total_ops = 0
            for num in nums:
                if num > P:
                    total_ops += (num - 1) // P
                if total_ops > maxOperations:
                    return False
            return total_ops <= maxOperations

        left = 1
        right = max(nums)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans