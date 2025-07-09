from collections import defaultdict

class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        remainder_counts = defaultdict(int)
        remainder_min_values = defaultdict(lambda: float('inf'))

        for num in nums:
            remainder = num % space
            remainder_counts[remainder] += 1
            remainder_min_values[remainder] = min(remainder_min_values[remainder], num)

        max_destroyed_targets = 0
        min_seed_value = float('inf')

        for remainder in remainder_counts:
            current_count = remainder_counts[remainder]
            current_min_seed = remainder_min_values[remainder]

            if current_count > max_destroyed_targets:
                max_destroyed_targets = current_count
                min_seed_value = current_min_seed
            elif current_count == max_destroyed_targets:
                min_seed_value = min(min_seed_value, current_min_seed)
        
        return min_seed_value