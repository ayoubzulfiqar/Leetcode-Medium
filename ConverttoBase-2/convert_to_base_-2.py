class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result_digits = []
        while n != 0:
            remainder = n % 2
            result_digits.append(str(remainder))
            n = (n - remainder) // -2
        
        return "".join(result_digits[::-1])