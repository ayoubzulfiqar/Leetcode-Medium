class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        n = len(word)
        div = [0] * n
        current_remainder = 0

        for i in range(n):
            digit = int(word[i])
            current_remainder = (current_remainder * 10 + digit) % m
            if current_remainder == 0:
                div[i] = 1
            else:
                div[i] = 0
        
        return div