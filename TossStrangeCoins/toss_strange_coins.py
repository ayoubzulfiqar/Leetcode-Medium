class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        dp = [0.0] * (target + 1)
        dp[0] = 1.0
        
        for p_head in prob:
            for j in range(target, -1, -1):
                prob_if_current_heads = 0.0
                if j > 0:
                    prob_if_current_heads = dp[j-1] * p_head
                
                prob_if_current_tails = dp[j] * (1 - p_head)
                
                dp[j] = prob_if_current_heads + prob_if_current_tails
                
        return dp[target]