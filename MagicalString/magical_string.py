def magicalString(n: int) -> int:
    if n == 0:
        return 0
    if n <= 3:
        return 1

    s = [1, 2, 2]
    head = 2
    current_char_to_add = 1

    while len(s) < n:
        count = s[head]
        
        for _ in range(count):
            s.append(current_char_to_add)
            if len(s) == n:
                break
        
        head += 1
        current_char_to_add = 3 - current_char_to_add

    count_ones = 0
    for i in range(n):
        if s[i] == 1:
            count_ones += 1
    
    return count_ones