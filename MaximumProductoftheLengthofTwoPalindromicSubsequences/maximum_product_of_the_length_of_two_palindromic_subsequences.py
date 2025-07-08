class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        lps_memo = {}

        for mask in range(1, 1 << n):
            sub_s = ""
            for i in range(n):
                if (mask >> i) & 1:
                    sub_s += s[i]
            
            L = len(sub_s)
            if L == 0:
                lps_memo[mask] = 0
                continue
            if L == 1:
                lps_memo[mask] = 1
                continue
            
            dp = [[0] * L for _ in range(L)]
            
            for i in range(L):
                dp[i][i] = 1
            
            for length in range(2, L + 1):
                for i in range(L - length + 1):
                    j = i + length - 1
                    if sub_s[i] == sub_s[j]:
                        dp[i][j] = 2 + (dp[i+1][j-1] if length > 2 else 0)
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            
            lps_memo[mask] = dp[0][L-1]
        
        max_product = 0
        
        for combined_mask in range(1, 1 << n):
            mask1 = combined_mask
            while mask1 > 0:
                mask2 = combined_mask ^ mask1
                
                if mask2 == 0:
                    mask1 = (mask1 - 1) & combined_mask
                    continue
                
                len1 = lps_memo[mask1]
                len2 = lps_memo[mask2]
                
                max_product = max(max_product, len1 * len2)
                
                mask1 = (mask1 - 1) & combined_mask
                
        return max_product