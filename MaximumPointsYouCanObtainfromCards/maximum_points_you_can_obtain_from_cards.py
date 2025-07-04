class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        total_sum = sum(cardPoints)

        window_size = n - k

        current_window_sum = sum(cardPoints[0:window_size])
        min_window_sum = current_window_sum

        for j in range(window_size, n):
            current_window_sum = current_window_sum - cardPoints[j - window_size] + cardPoints[j]
            min_window_sum = min(min_window_sum, current_window_sum)

        return total_sum - min_window_sum