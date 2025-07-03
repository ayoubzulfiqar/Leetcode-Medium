class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        remainder_counts = [0] * 60
        count = 0

        for t in time:
            remainder = t % 60
            
            if remainder == 0:
                count += remainder_counts[0]
            else:
                count += remainder_counts[60 - remainder]
            
            remainder_counts[remainder] += 1
            
        return count