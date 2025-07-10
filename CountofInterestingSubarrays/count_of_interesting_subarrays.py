class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        count = 0
        current_prefix_sum = 0
        
        remainder_counts = {0: 1} 
        
        for num in nums:
            val = 1 if num % modulo == k else 0
            
            current_prefix_sum += val
            
            current_remainder = current_prefix_sum % modulo
            
            desired_prev_remainder = (current_remainder - k + modulo) % modulo
            
            count += remainder_counts.get(desired_prev_remainder, 0)
            
            remainder_counts[current_remainder] = remainder_counts.get(current_remainder, 0) + 1
            
        return count