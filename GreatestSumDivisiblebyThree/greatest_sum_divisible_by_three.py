class Solution:
    def maxSumDivisibleByThree(self, nums: list[int]) -> int:
        total_sum = 0
        
        min1_1 = float('inf') 
        min1_2 = float('inf') 
        
        min2_1 = float('inf') 
        min2_2 = float('inf') 
        
        for num in nums:
            total_sum += num
            
            if num % 3 == 1:
                if num < min1_1:
                    min1_2 = min1_1
                    min1_1 = num
                elif num < min1_2:
                    min1_2 = num
            elif num % 3 == 2:
                if num < min2_1:
                    min2_2 = min2_1
                    min2_1 = num
                elif num < min2_2:
                    min2_2 = num
                    
        if total_sum % 3 == 0:
            return total_sum
        
        elif total_sum % 3 == 1:
            subtract_option1 = min1_1
            subtract_option2 = min2_1 + min2_2
            
            to_subtract = min(subtract_option1, subtract_option2)
            
            if to_subtract == float('inf'):
                return 0
            else:
                return total_sum - to_subtract
            
        else: # total_sum % 3 == 2
            subtract_option1 = min2_1
            subtract_option2 = min1_1 + min1_2
            
            to_subtract = min(subtract_option1, subtract_option2)
            
            if to_subtract == float('inf'):
                return 0
            else:
                return total_sum - to_subtract