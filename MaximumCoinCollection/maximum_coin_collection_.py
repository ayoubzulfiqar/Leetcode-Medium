def max_coin_collection(coins):
    if not coins or not coins[0]:
        return 0
    
    rows = len(coins)
    cols = len(coins[0])
    
    dp = [[0] * cols for _ in range(rows)]
    
    dp[0][0] = coins[0][0]
    
    for j in range(1, cols):
        dp[0][j] = coins[0][j] + dp[0][j-1]
        
    for i in range(1, rows):
        dp[i][0] = coins[i][0] + dp[i-1][0]
        
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = coins[i][j] + max(dp[i-1][j], dp[i][j-1])
            
    return dp[rows-1][cols-1]