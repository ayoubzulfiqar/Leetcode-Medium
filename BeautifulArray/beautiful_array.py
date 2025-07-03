_memo = {1: [1]}

def beautifulArray(n: int) -> list[int]:
    if n in _memo:
        return _memo[n]

    odd_count = (n + 1) // 2
    odd_elements_transformed = [2 * x - 1 for x in beautifulArray(odd_count)]

    even_count = n // 2
    even_elements_transformed = [2 * x for x in beautifulArray(even_count)]
    
    result = odd_elements_transformed + even_elements_transformed
    _memo[n] = result
    return result