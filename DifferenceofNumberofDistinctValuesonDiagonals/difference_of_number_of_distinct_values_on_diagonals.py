class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        
        answer = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                left_above_set = set()
                k = 1
                while True:
                    prev_r = r - k
                    prev_c = c - k
                    if prev_r >= 0 and prev_c >= 0:
                        left_above_set.add(grid[prev_r][prev_c])
                        k += 1
                    else:
                        break
                left_above_count = len(left_above_set)
                
                right_below_set = set()
                k = 1
                while True:
                    next_r = r + k
                    next_c = c + k
                    if next_r < m and next_c < n:
                        right_below_set.add(grid[next_r][next_c])
                        k += 1
                    else:
                        break
                right_below_count = len(right_below_set)
                
                answer[r][c] = abs(left_above_count - right_below_count)
                
        return answer