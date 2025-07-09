def removeOnes(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    min_flips = float('inf')

    for first_row_flip_state in [0, 1]:
        current_flips = first_row_flip_state

        r = [0] * m
        c = [0] * n

        r[0] = first_row_flip_state

        for j in range(n):
            c[j] = grid[0][j] ^ r[0]
            current_flips += c[j]

        possible = True
        for i in range(1, m):
            r[i] = grid[i][0] ^ c[0]
            current_flips += r[i]

            for j in range(1, n):
                if (grid[i][j] ^ r[i] ^ c[j]) != 0:
                    possible = False
                    break
            if not possible:
                break
        
        if possible:
            min_flips = min(min_flips, current_flips)
    
    return min_flips