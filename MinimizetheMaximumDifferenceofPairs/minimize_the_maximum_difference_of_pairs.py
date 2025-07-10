class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def can_form_p_pairs(diff_limit: int) -> bool:
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= diff_limit:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        low = 0
        high = nums[n-1] - nums[0]
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if can_form_p_pairs(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans