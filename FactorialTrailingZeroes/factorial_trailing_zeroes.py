class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        current_power_of_5 = 5
        while n >= current_power_of_5:
            count += n // current_power_of_5
            current_power_of_5 *= 5
        return count