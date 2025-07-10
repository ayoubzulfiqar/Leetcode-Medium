class Solution:
    def countWays(self, ranges: list[list[int]]) -> int:
        MOD = 10**9 + 7

        ranges.sort()

        num_components = 0
        current_merged_end = -1

        for start, end in ranges:
            if start > current_merged_end:
                num_components += 1
                current_merged_end = end
            else:
                current_merged_end = max(current_merged_end, end)
        
        return pow(2, num_components, MOD)