class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        arr.sort()
        
        arr_set = set(arr)
        
        dp = {x: 1 for x in arr}
        
        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                factor1 = arr[j]
                
                if factor1 * factor1 > num:
                    break
                
                if num % factor1 == 0:
                    factor2 = num // factor1
                    
                    if factor2 in arr_set:
                        if factor1 == factor2:
                            dp[num] = (dp[num] + dp[factor1] * dp[factor2]) % MOD
                        else:
                            dp[num] = (dp[num] + dp[factor1] * dp[factor2] * 2) % MOD
        
        total_trees = sum(dp.values()) % MOD
        
        return total_trees