class Solution:
    def solve(self, n: int, edges: list[list[int]], k: int, t: int) -> int:
        dp = [[-float('inf')] * n for _ in range(k + 1)]

        for i in range(n):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for u, v, w in edges:
                if dp[j-1][u] != -float('inf'):
                    dp[j][v] = max(dp[j][v], dp[j-1][u] + w)

        max_overall_weight = -1

        for v in range(n):
            current_path_weight = dp[k][v]
            if current_path_weight != -float('inf') and current_path_weight < t:
                max_overall_weight = max(max_overall_weight, current_path_weight)

        return max_overall_weight