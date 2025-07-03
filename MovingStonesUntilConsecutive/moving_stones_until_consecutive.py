class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        stones = sorted([a, b, c])
        x, y, z = stones[0], stones[1], stones[2]

        min_moves = 0
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2

        max_moves = (y - x - 1) + (z - y - 1)

        return [min_moves, max_moves]