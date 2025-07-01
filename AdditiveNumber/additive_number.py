class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid(prev1_str: str, prev2_str: str, current_idx: int) -> bool:
            if current_idx == n:
                return True

            n1 = int(prev1_str)
            n2 = int(prev2_str)
            
            sum_val = n1 + n2
            sum_str = str(sum_val)
            
            if not num.startswith(sum_str, current_idx):
                return False
            
            return is_valid(prev2_str, sum_str, current_idx + len(sum_str))

        for i in range(1, n): 
            num1_str = num[0:i]
            
            if len(num1_str) > 1 and num1_str[0] == '0':
                break 

            for j in range(1, n - i): 
                num2_str = num[i : i + j]
                
                if len(num2_str) > 1 and num2_str[0] == '0':
                    break 

                if is_valid(num1_str, num2_str, i + j):
                    return True
        
        return False