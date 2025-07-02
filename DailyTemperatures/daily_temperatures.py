class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] # Stores indices

        for i in range(n):
            current_temp = temperatures[i]
            
            # While stack is not empty AND current temperature is warmer than the temperature at the index on top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            # Push the current index onto the stack
            stack.append(i)
            
        return answer