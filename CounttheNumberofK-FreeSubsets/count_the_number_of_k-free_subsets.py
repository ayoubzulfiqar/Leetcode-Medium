def count_k_free_subsets(N, K):
    if N <= 0:
        return 1

    K = abs(K)
    if K == 0:
        return 2**N

    fib_dp = [0] * (N + 1)
    fib_dp[0] = 1
    if N >= 1:
        fib_dp[1] = 2
    
    for i in range(2, N + 1):
        fib_dp[i] = fib_dp[i-1] + fib_dp[i-2]
        
    total_k_free_subsets = 1
    
    for start_val in range(1, K + 1):
        if start_val > N:
            break 
            
        chain_length = (N - start_val) // K + 1
        
        total_k_free_subsets *= fib_dp[chain_length]
        
    return total_k_free_subsets