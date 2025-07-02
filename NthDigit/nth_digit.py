class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        
        n -= 1 
        
        num_index_in_block = n // digits
        actual_number = start + num_index_in_block
        
        digit_index_in_num = n % digits
        
        s_num = str(actual_number)
        
        return int(s_num[digit_index_in_num])