class Solution:
    def sumOfDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)
        
        first_num_str = str(nums[0])
        num_digits = len(first_num_str)
        
        total_digit_differences = 0
        
        for i in range(num_digits):
            divisor = 10**(num_digits - 1 - i)
            
            digit_counts = [0] * 10
            
            for num in nums:
                digit = (num // divisor) % 10
                digit_counts[digit] += 1
            
            diff_pairs_at_current_position = 0
            for count_d in digit_counts:
                diff_pairs_at_current_position += count_d * (n - count_d)
            
            total_digit_differences += diff_pairs_at_current_position // 2
            
        return total_digit_differences