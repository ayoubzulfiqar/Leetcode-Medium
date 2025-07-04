class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        
        for start_digit in range(1, 10):
            current_num = start_digit
            for next_digit in range(start_digit + 1, 10):
                current_num = current_num * 10 + next_digit
                
                if low <= current_num <= high:
                    res.append(current_num)
                elif current_num > high:
                    break
        
        res.sort()
        
        return res