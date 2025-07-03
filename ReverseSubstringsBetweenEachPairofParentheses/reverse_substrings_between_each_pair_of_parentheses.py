class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_segment = []

        for char in s:
            if char == '(':
                stack.append(current_segment)
                current_segment = []
            elif char == ')':
                reversed_segment = current_segment[::-1]
                prev_segment = stack.pop()
                prev_segment.extend(reversed_segment)
                current_segment = prev_segment
            else:
                current_segment.append(char)
        
        return "".join(current_segment)