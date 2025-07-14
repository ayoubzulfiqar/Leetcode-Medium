class Solution:
    def minK(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        m = len(queries)
        initial_nums = list(nums)

        def check(k_val):
            for i in range(n):
                target = initial_nums[i]
                if target == 0:
                    continue

                dp = [False] * (target + 1)
                dp[0] = True

                for j in range(k_val):
                    l, r, val = queries[j]

                    if l <= i <= r:
                        for s in range(target, val - 1, -1):
                            dp[s] = dp[s] or dp[s - val]
                
                if not dp[target]:
                    return False
            
            return True

        low = 0
        high = m
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans