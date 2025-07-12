class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        remainder_counts = [0] * 24
        count = 0
        for hour in hours:
            remainder = hour % 24
            complement_remainder = (24 - remainder) % 24
            count += remainder_counts[complement_remainder]
            remainder_counts[remainder] += 1
        return count