class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:
        prefix_sum_map = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            if (current_sum - target) in prefix_sum_map:
                count += 1
                current_sum = 0
                prefix_sum_map = {0: 1}
            else:
                prefix_sum_map[current_sum] = 1
        
        return count