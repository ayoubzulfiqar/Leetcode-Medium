class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operation = '+'
        
        s = s + '+' 
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == ' ':
                continue
            else: 
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    operand1 = stack.pop()
                    stack.append(operand1 * current_number)
                elif operation == '/':
                    operand1 = stack.pop()
                    stack.append(int(float(operand1) / current_number))
                
                operation = char
                current_number = 0
                
        return sum(stack)