def solve(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]