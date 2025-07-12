def find_pattern_in_matrix(matrix, pattern):
    R = len(matrix)
    C = len(matrix[0]) if R > 0 else 0
    
    r = len(pattern)
    c = len(pattern[0]) if r > 0 else 0

    if r == 0:
        return True
    
    if R == 0 or C == 0:
        return False
    
    if r > R or c > C:
        return False

    for i in range(R - r + 1):
        for j in range(C - c + 1):
            match_found_at_current_pos = True
            for x in range(r):
                for y in range(c):
                    if matrix[i + x][j + y] != pattern[x][y]:
                        match_found_at_current_pos = False
                        break
                if not match_found_at_current_pos:
                    break
            
            if match_found_at_current_pos:
                return True

    return False