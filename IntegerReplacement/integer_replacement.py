class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3:
                    n -= 1
                elif (n % 4) == 1:
                    n -= 1
                else:
                    n += 1
            operations += 1
        return operations