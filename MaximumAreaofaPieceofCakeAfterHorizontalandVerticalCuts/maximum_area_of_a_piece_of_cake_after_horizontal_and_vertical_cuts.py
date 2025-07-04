class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        MOD = 10**9 + 7

        horizontalCuts.sort()
        max_h_diff = 0
        
        all_h_cuts = [0] + horizontalCuts + [h]
        for i in range(1, len(all_h_cuts)):
            max_h_diff = max(max_h_diff, all_h_cuts[i] - all_h_cuts[i-1])

        verticalCuts.sort()
        max_w_diff = 0
        
        all_v_cuts = [0] + verticalCuts + [w]
        for i in range(1, len(all_v_cuts)):
            max_w_diff = max(max_w_diff, all_v_cuts[i] - all_v_cuts[i-1])
        
        return (max_h_diff * max_w_diff) % MOD