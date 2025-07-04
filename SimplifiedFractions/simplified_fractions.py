import math

def simplifiedFractions(n: int) -> list[str]:
    result = []
    for d in range(2, n + 1):
        for num in range(1, d):
            if math.gcd(num, d) == 1:
                result.append(f"{num}/{d}")
    return result