def smallest_greater_multiple_two_digits(n: int) -> int | None:
    for m in range(n + 1, 100):
        for k in range(10, 100):
            if m % k == 0:
                return m
    return None