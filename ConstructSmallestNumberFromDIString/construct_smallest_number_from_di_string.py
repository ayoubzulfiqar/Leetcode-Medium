class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = []
        stack = []
        current_digit = 1

        for i in range(n + 1):
            stack.append(current_digit)
            current_digit += 1

            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        
        return "".join(result)