import collections

class Solution:
    _power_of_2_digit_counts = set()

    @classmethod
    def _precompute(cls):
        if not cls._power_of_2_digit_counts:
            for i in range(31):
                p = 1 << i
                cls._power_of_2_digit_counts.add(frozenset(collections.Counter(str(p)).items()))

    def reorderedPowerOf2(self, n: int) -> bool:
        Solution._precompute()
        n_digit_counts = frozenset(collections.Counter(str(n)).items())
        return n_digit_counts in Solution._power_of_2_digit_counts