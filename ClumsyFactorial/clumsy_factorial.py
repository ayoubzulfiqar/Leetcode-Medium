class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6

        terms = []
        current_val = n
        op_type = 0  # 0:*, 1:/, 2:+, 3:-

        for i in range(n - 1, 0, -1):
            if op_type == 0:  # Multiplication
                current_val *= i
            elif op_type == 1:  # Floor Division
                current_val //= i
            elif op_type == 2:  # Addition
                terms.append(current_val)
                terms.append('+')
                current_val = i
            elif op_type == 3:  # Subtraction
                terms.append(current_val)
                terms.append('-')
                current_val = i
            
            op_type = (op_type + 1) % 4
        
        terms.append(current_val)

        result = terms[0]
        for j in range(1, len(terms) - 1, 2):
            op = terms[j]
            num = terms[j+1]
            if op == '+':
                result += num
            elif op == '-':
                result -= num
        
        return result