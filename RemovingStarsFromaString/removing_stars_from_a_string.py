class Solution:
    def removeStars(self, s: str) -> str:
        result_chars = []
        for char in s:
            if char != '*':
                result_chars.append(char)
            else:
                result_chars.pop()
        return "".join(result_chars)