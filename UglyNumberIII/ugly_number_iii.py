import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            return math.gcd(x, y)

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        lcm_ab = lcm(a, b)
        lcm_ac = lcm(a, c)
        lcm_bc = lcm(b, c)
        
        lcm_abc = lcm(lcm_ab, c)

        def count_ugly_numbers_le(num):
            total = num // a + num // b + num // c
            total -= num // lcm_ab
            total -= num // lcm_ac
            total -= num // lcm_bc
            total += num // lcm_abc
            return total

        low = 1
        high = 2 * 10**9
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if count_ugly_numbers_le(mid) >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans