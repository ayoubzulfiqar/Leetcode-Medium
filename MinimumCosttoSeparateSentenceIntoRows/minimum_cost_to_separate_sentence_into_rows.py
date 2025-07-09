def minCostToSeparateSentenceIntoRows(words: list[str], valid_lengths: list[int]) -> int:
    n = len(words)

    if n == 0:
        return 0
    
    if not valid_lengths:
        K_max = 0
    else:
        K_max = max(valid_lengths)

    dp = [float('inf')] * (n + 1)
    dp[n] = 0

    for i in range(n - 1, -1, -1):
        current_line_length = 0
        for j in range(i, n):
            word_len = len(words[j])
            
            if i == j:
                current_line_length = word_len
            else:
                current_line_length += (1 + word_len)
            
            line_cost = 0
            if current_line_length > K_max:
                line_cost = (current_line_length - K_max) ** 2
            
            total_cost_for_this_segment = line_cost + dp[j+1]
            
            dp[i] = min(dp[i], total_cost_for_this_segment)
    
    return dp[0]