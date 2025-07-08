def maximumScore(a: int, b: int, c: int) -> int:
    piles = sorted([a, b, c])
    x, y, z = piles[0], piles[1], piles[2]
    
    return min((x + y + z) // 2, x + y)