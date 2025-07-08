class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        dp = [False] * n
        dp[0] = True

        prefix_reachable_count = [0] * n
        prefix_reachable_count[0] = 1 

        for i in range(1, n):
            prefix_reachable_count[i] = prefix_reachable_count[i-1]

            if s[i] == '1':
                continue

            left_idx_for_check = i - maxJump
            right_idx_for_check = i - minJump
            
            count_in_window = 0
            if right_idx_for_check >= 0:
                count_in_window = prefix_reachable_count[right_idx_for_check]
            
            if left_idx_for_check > 0:
                count_in_window -= prefix_reachable_count[left_idx_for_check - 1]
            
            if count_in_window > 0:
                dp[i] = True
                prefix_reachable_count[i] += 1
        
        return dp[n-1]