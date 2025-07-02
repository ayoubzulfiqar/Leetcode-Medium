class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total_count = 10 
        current_product = 9 
        available_digits = 9 

        for i in range(2, n + 1):
            if available_digits == 0:
                break
            
            current_product *= available_digits
            total_count += current_product
            available_digits -= 1
            
        return total_count