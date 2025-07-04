class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            sum_without_carry = a ^ b
            carry = (a & b) << 1
            a = sum_without_carry
            b = carry
        return a