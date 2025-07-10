class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def check(target: int, s: str, index: int, current_sum: int) -> bool:
            if index == len(s):
                return current_sum == target
            
            if current_sum > target:
                return False
            
            for j in range(index, len(s)):
                substring_val = int(s[index : j + 1])
                
                if current_sum + substring_val > target:
                    break 
                
                if check(target, s, j + 1, current_sum + substring_val):
                    return True
                    
            return False

        punishment_sum = 0
        
        for i in range(1, n + 1):
            square = i * i
            s_square = str(square)
            
            if check(i, s_square, 0, 0):
                punishment_sum += square
                
        return punishment_sum