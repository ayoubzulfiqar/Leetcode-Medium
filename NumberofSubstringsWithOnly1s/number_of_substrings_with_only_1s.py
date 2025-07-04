def numSub(s: str) -> int:
    MOD = 10**9 + 7
    total_substrings = 0
    current_consecutive_ones = 0

    for char in s:
        if char == '1':
            current_consecutive_ones += 1
            total_substrings = (total_substrings + current_consecutive_ones) % MOD
        else:
            current_consecutive_ones = 0
            
    return total_substrings