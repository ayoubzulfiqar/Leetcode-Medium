class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner_position = 0
        for i in range(2, n + 1):
            winner_position = (winner_position + k) % i
        return winner_position + 1