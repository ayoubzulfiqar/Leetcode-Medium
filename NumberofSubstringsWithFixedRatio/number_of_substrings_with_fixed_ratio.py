def numberOfSubstringsWithFixedRatio(s: str, ratio_a: int, ratio_b: int) -> int:
    count_a = 0
    count_b = 0
    total_subarrays = 0
    
    freq = {0: 1} 

    for char in s:
        if char == 'a':
            count_a += 1
        elif char == 'b':
            count_b += 1
        
        current_diff = count_a * ratio_b - count_b * ratio_a
        
        if current_diff in freq:
            total_subarrays += freq[current_diff]
            freq[current_diff] += 1
        else:
            freq[current_diff] = 1
            
    return total_subarrays