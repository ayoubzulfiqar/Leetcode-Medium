import math

class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        total_sum = 0
        stack = [math.inf] 
        
        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                total_sum += mid * min(stack[-1], x)
            stack.append(x)
            
        while len(stack) > 2:
            total_sum += stack.pop() * stack[-1]
            
        return total_sum