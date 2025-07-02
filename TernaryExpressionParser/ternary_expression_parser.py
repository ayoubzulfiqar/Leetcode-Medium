class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        n = len(expression)

        i = n - 1
        while i >= 0:
            char = expression[i]

            if char.isdigit() or char == 'T' or char == 'F':
                stack.append(char)
            elif char == ':':
                pass
            elif char == '?':
                true_value = stack.pop()
                false_value = stack.pop()
                condition = expression[i-1] 
                
                if condition == 'T':
                    stack.append(true_value)
                else:
                    stack.append(false_value)
                
                i -= 1 
            
            i -= 1
        
        return stack[0]