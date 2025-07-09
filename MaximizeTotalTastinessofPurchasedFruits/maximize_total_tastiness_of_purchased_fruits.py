def maximize_total_tastiness(fruits, budget):
    dp = [0] * (budget + 1)

    for tastiness, cost in fruits:
        for c in range(budget, cost - 1, -1):
            dp[c] = max(dp[c], dp[c - cost] + tastiness)

    return dp[budget]