import math

def maxScore(nums: list[int]) -> int:
    n = len(nums)
    memo = {}

    def solve(mask):
        if mask == (1 << n) - 1:
            return 0
        if mask in memo:
            return memo[mask]

        k = bin(mask).count('1') // 2 + 1
        max_current_score = 0

        first_unused_idx = -1
        for i in range(n):
            if not ((mask >> i) & 1):
                first_unused_idx = i
                break
        
        for j in range(first_unused_idx + 1, n):
            if not ((mask >> j) & 1):
                new_mask = mask | (1 << first_unused_idx) | (1 << j)
                current_pair_score = math.gcd(nums[first_unused_idx], nums[j]) * k
                max_current_score = max(max_current_score, current_pair_score + solve(new_mask))
        
        memo[mask] = max_current_score
        return max_current_score

    return solve(0)