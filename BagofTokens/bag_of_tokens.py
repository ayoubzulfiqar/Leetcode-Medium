class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        left = 0
        right = n - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score >= 1 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        
        return max_score