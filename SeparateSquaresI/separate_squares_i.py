class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        total_area = 0.0
        min_y_possible = float('inf')
        max_yl_possible = float('-inf')

        for x, y, l in squares:
            square_area = float(l * l)
            total_area += square_area
            min_y_possible = min(min_y_possible, float(y))
            max_yl_possible = max(max_yl_possible, float(y + l))

        target_area = total_area / 2.0

        def calculate_area_above(H: float) -> float:
            current_area_above = 0.0
            for x_s, y_s, l_s in squares:
                y_float = float(y_s)
                l_float = float(l_s)
                
                if y_float >= H:
                    current_area_above += l_float * l_float
                elif y_float + l_float > H:
                    current_area_above += l_float * (y_float + l_float - H)
            return current_area_above

        low = min_y_possible
        high = max_yl_possible

        for _ in range(100):
            mid = (low + high) / 2.0
            area_above_mid = calculate_area_above(mid)

            if area_above_mid > target_area:
                low = mid
            else:
                high = mid
        
        return high