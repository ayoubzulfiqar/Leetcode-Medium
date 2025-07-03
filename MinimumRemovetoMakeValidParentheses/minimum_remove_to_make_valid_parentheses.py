class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        while stack:
            to_remove.add(stack.pop())
            
        result_chars = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result_chars.append(char)
                
        return "".join(result_chars)