class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        max_len = 0
        current_sum = 0
        # Map to store (sum: first_index)
        sum_map = {0: -1} 

        for i, num in enumerate(nums):
            if num == 0:
                current_sum -= 1
            else:  # num == 1
                current_sum += 1
            
            if current_sum in sum_map:
                max_len = max(max_len, i - sum_map[current_sum])
            else:
                sum_map[current_sum] = i
                
        return max_len