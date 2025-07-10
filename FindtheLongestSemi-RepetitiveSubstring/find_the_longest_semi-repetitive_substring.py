def longestSemiRepetitiveSubstring(s: str) -> int:
    n = len(s)
    
    if n == 1:
        return 1
    
    max_len = 0
    left = 0
    adjacent_pairs_count = 0
    
    for right in range(n):
        if right > 0 and s[right] == s[right - 1]:
            adjacent_pairs_count += 1
        
        while adjacent_pairs_count > 1:
            if s[left] == s[left + 1]:
                adjacent_pairs_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len