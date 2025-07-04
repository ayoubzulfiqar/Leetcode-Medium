class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                dp[r+1][c+1] = mat[r][c] + dp[r][c+1] + dp[r+1][c] - dp[r][c]

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                answer[i][j] = dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]

        return answer