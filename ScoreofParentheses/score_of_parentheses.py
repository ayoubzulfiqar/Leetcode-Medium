class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current_score = 0

        for char in s:
            if char == '(':
                stack.append(current_score)
                current_score = 0
            else:  # char == ')'
                prev_score = stack.pop()
                current_score = prev_score + max(1, 2 * current_score)
        
        return current_score