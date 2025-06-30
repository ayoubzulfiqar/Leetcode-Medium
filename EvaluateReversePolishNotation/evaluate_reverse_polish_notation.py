class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                # It's an operand (number), convert to integer and push
                stack.append(int(token))
            else:
                # It's an operator, pop two operands, perform operation, and push result
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "/":
                    # Division truncates toward zero.
                    # Python's int() on the result of float division achieves this.
                    result = int(operand1 / operand2)
                
                stack.append(result)
        
        # The final result is the only element left on the stack
        return stack[0]