class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if k == 0:
            if num % 10 == 0:
                return 1
            else:
                return -1

        for m in range(1, num // k + 1):
            # We are looking for 'm' positive integers, each ending in 'k', that sum to 'num'.
            # Let these integers be x_1, x_2, ..., x_m.
            # Each x_i can be written as 10 * a_i + k, where a_i >= 0.
            # The sum is: sum(10 * a_i + k) = 10 * sum(a_i) + m * k = num.
            # This implies two conditions:
            # 1. (num - m * k) must be non-negative.
            #    This is implicitly handled by the loop range `m <= num // k`,
            #    which means `m * k <= num`, so `num - m * k >= 0`.
            # 2. (num - m * k) must be a multiple of 10.
            #    This is because 10 * sum(a_i) is always a multiple of 10.
            if (num - m * k) % 10 == 0:
                return m

        return -1