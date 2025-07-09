class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_subarrays = 0
        current_zero_count = 0
        
        for num in nums:
            if num == 0:
                current_zero_count += 1
            else:
                # If a block of zeros just ended, calculate subarrays from that block
                # The number of subarrays from k zeros is k * (k + 1) / 2
                total_subarrays += current_zero_count * (current_zero_count + 1) // 2
                current_zero_count = 0 # Reset count for the next potential block of zeros
                
        # After the loop, if the array ends with zeros, add the count for the last block
        total_subarrays += current_zero_count * (current_zero_count + 1) // 2
        
        return total_subarrays