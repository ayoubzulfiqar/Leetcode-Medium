def countColoredCells(n: int) -> int:
    """
    Calculates the total number of colored cells at the end of n minutes.

    Args:
        n: The number of minutes.

    Returns:
        The total number of colored cells.
    """
    if n == 1:
        return 1
    
    # The pattern of colored cells forms a diamond shape.
    # At minute 1, there is 1 cell (Manhattan distance 0 from center).
    # At minute 2, cells within Manhattan distance 1 from center are colored.
    # At minute n, cells within Manhattan distance (n-1) from center are colored.
    # The number of cells (x,y) such that |x| + |y| <= k is 2*k*(k+1) + 1.
    # Here, k = n - 1.
    k = n - 1
    return 2 * k * (k + 1) + 1