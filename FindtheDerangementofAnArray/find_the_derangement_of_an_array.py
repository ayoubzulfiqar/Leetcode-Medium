def derangements(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 0

    d_prev2 = 1
    d_prev1 = 0

    for i in range(2, n + 1):
        d_current = (i - 1) * (d_prev1 + d_prev2)
        d_prev2 = d_prev1
        d_prev1 = d_current
    
    return d_prev1