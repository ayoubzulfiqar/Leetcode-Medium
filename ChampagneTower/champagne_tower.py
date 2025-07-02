class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        glasses[0][0] = float(poured)

        for r in range(query_row):
            for c in range(r + 1):
                if glasses[r][c] > 1.0:
                    excess = glasses[r][c] - 1.0
                    glasses[r+1][c] += excess / 2.0
                    glasses[r+1][c+1] += excess / 2.0
        
        return min(1.0, glasses[query_row][query_glass])