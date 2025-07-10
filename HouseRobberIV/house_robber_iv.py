class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def check(max_val: int) -> bool:
            """
            Checks if it's possible to rob at least k houses
            such that the money in each robbed house is <= max_val.
            """
            count = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= max_val:
                    count += 1
                    i += 2  # Skip the next house (adjacent)
                else:
                    i += 1  # Cannot rob this house, move to the next
            return count >= k

        low = min(nums)
        high = max(nums)
        ans = high  # Initialize with a value that is guaranteed to be a possible answer

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1  # Try to find a smaller capability
            else:
                low = mid + 1   # Need a larger capability

        return ans