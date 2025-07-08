import collections

class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def rev(x: int) -> int:
            s = str(x)
            return int(s[::-1])

        diff_counts = collections.defaultdict(int)
        
        for num in nums:
            diff = num - rev(num)
            diff_counts[diff] += 1
        
        nice_pairs_count = 0
        for freq in diff_counts.values():
            if freq >= 2:
                pairs_for_this_diff = (freq * (freq - 1)) // 2
                nice_pairs_count = (nice_pairs_count + pairs_for_this_diff) % MOD
                
        return nice_pairs_count