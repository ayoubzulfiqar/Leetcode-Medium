class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2
        K = n - 1
        
        K = min(K, N - K)
        
        res = 1
        for i in range(K):
            res = res * (N - i) // (i + 1)
        
        return res