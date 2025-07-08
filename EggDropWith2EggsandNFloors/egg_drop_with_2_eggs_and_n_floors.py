class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = 0
        floors_covered = 0
        while floors_covered < n:
            moves += 1
            floors_covered += moves
        return moves