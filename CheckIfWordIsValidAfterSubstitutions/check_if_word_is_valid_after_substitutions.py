class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == 'a' or char == 'b':
                stack.append(char)
            elif char == 'c':
                if len(stack) >= 2 and stack[-2] == 'a' and stack[-1] == 'b':
                    stack.pop()
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0