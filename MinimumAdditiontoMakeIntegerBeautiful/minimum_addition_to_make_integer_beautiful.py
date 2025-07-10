class Solution:
    def _sum_digits(self, num: int) -> int:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s

    def minimumBeautifulAddition(self, n: int, target: int) -> int:
        if self._sum_digits(n) <= target:
            return 0

        ans = 0
        power_of_10 = 1

        while self._sum_digits(n) > target:
            current_digit = (n // power_of_10) % 10

            if current_digit == 0:
                power_of_10 *= 10
                continue
            
            add_value = (10 - current_digit) * power_of_10
            
            ans += add_value
            n += add_value
            
            power_of_10 *= 10
            
        return ans