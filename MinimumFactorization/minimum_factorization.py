```python
class Solution:
    def smallestFactorization(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        digits = []
        for d in range(9, 1, -1):
            while n % d == 0:
                digits.append(d)
                n //= d

        if n > 1:
            return 0

        digits.sort()

        result_str = "".join(map(str, digits))
        
        result = int(result_str)

        MAX_INT_32 = 2**31 - 1
        if result > MAX_INT_32:
            return 0

        return result

```