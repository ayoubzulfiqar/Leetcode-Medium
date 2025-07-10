class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1
            
            for j in range(i):
                current_word = s[j:i]
                if current_word in dictionary_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]