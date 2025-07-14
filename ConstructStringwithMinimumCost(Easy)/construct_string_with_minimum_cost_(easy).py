class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(len(words)):
                word = words[j]
                cost = costs[j]
                word_len = len(word)

                if i >= word_len and target[i - word_len:i] == word:
                    if dp[i - word_len] != float('inf'):
                        dp[i] = min(dp[i], dp[i - word_len] + cost)

        return dp[n] if dp[n] != float('inf') else -1