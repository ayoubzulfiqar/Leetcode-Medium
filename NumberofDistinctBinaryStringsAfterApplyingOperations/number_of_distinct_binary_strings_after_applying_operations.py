def solve(N: int) -> int:
    if not isinstance(N, int):
        raise TypeError("Input N must be an integer.")
    if N < 0:
        raise ValueError("Length N cannot be negative.")
    return 2**N