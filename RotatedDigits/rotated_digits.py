class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        # Digits that rotate to a different valid digit
        diff_digits = {2, 5, 6, 9}
        # Digits that become invalid upon rotation
        invalid_digits = {3, 4, 7}
        
        for i in range(1, n + 1):
            is_valid_rotation = True
            contains_diff_digit = False
            
            temp_num = i
            
            while temp_num > 0:
                digit = temp_num % 10
                
                if digit in invalid_digits:
                    is_valid_rotation = False
                    break 
                
                if digit in diff_digits:
                    contains_diff_digit = True
                
                temp_num //= 10
            
            if is_valid_rotation and contains_diff_digit:
                count += 1
                
        return count