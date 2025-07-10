class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)

        beautiful_strings = set()
        current_power_of_5 = 1
        max_val_for_15_bits = (1 << 15) - 1 
        
        while current_power_of_5 <= max_val_for_15_bits:
            binary_rep = bin(current_power_of_5)[2:]
            beautiful_strings.add(binary_rep)
            current_power_of_5 *= 5

        dp = [float('inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue

            for j in range(i, n):
                substring = s[i : j + 1]
                
                if substring in beautiful_strings:
                    if dp[j + 1] != float('inf'):
                        dp[i] = min(dp[i], 1 + dp[j + 1])

        if dp[0] == float('inf'):
            return -1
        else:
            return dp[0]