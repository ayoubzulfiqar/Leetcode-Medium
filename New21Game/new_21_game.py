class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        current_prob_sum = 1.0
        ans = 0.0

        for i in range(1, n + 1):
            dp[i] = current_prob_sum / maxPts

            if i < k:
                current_prob_sum += dp[i]
            else:
                ans += dp[i]

            if i >= maxPts:
                if (i - maxPts) < k:
                    current_prob_sum -= dp[i - maxPts]

        return ans