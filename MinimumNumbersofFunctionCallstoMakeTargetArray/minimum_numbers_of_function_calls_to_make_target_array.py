class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total_increments = 0
        max_doubles = 0

        for num in nums:
            current_increments = 0
            temp_num = num 
            
            # Count increment operations (number of set bits)
            while temp_num > 0:
                if temp_num % 2 == 1:
                    current_increments += 1
                temp_num //= 2
            
            total_increments += current_increments
            
            # Determine the maximum number of doubling operations needed
            # This is equivalent to floor(log2(num)) for num > 0,
            # or num.bit_length() - 1 in Python.
            if num > 0:
                max_doubles = max(max_doubles, num.bit_length() - 1)
        
        return total_increments + max_doubles