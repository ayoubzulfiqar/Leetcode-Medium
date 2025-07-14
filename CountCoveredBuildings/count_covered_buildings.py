class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        min_y_in_row = {}
        max_y_in_row = {}
        min_x_in_col = {}
        max_x_in_col = {}

        for x, y in buildings:
            min_y_in_row[x] = min(min_y_in_row.get(x, float('inf')), y)
            max_y_in_row[x] = max(max_y_in_row.get(x, float('-inf')), y)

            min_x_in_col[y] = min(min_x_in_col.get(y, float('inf')), x)
            max_x_in_col[y] = max(max_x_in_col.get(y, float('-inf')), x)

        covered_count = 0
        for x, y in buildings:
            has_left = (min_y_in_row[x] < y)
            has_right = (max_y_in_row[x] > y)
            has_above = (min_x_in_col[y] < x)
            has_below = (max_x_in_col[y] > x)
            
            if has_left and has_right and has_above and has_below:
                covered_count += 1
                
        return covered_count