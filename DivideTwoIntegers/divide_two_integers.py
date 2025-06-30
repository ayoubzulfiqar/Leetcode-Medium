class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negative = (dividend < 0) != (divisor < 0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        for i in range(31, -1, -1):
            if (abs_divisor << i) <= abs_dividend:
                abs_dividend -= (abs_divisor << i)
                quotient += (1 << i)

        if negative:
            quotient = -quotient

        if quotient > MAX_INT:
            return MAX_INT
        if quotient < MIN_INT:
            return MIN_INT

        return quotient