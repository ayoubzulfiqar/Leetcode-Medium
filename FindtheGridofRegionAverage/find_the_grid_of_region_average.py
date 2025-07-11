```python
class Solution:
    def resultGrid(self, image: list[list[int]], threshold: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])

        result = [row[:] for row in image]

        sum_region_averages = [[0] * n for _ in range(m)]
        count_regions = [[0] * n for _ in range(m)]

        def is_valid_region(r_start, c_start):
            # Check horizontal adjacencies within the 3x3 subgrid
            for i in range(r_start, r_start + 3):
                for j in range(c_start, c_start + 2):
                    if abs(image[i][j] - image[i][j+1]) > threshold:
                        return False
            # Check vertical adjacencies within the 3x3 subgrid
            for i in range(r_start, r_start + 2):
                for j in range(c_start, c_start + 3):
                    if abs(image[i][j] - image[i+1][j]) > threshold:
                        return False
            return True

        for r in range(m - 2):
            for c in range(n - 2):
                if is_valid_region(r, c):
                    current_region_sum = 0
                    for i in range(r, r + 3):
                        for j in range(c, c + 3):
                            current_region_sum += image[i][j]
                    
                    region_avg = current_region_sum // 9

                    for i in range(r, r + 3):
                        for j in range(c, c + 3):
                            sum_region_averages[i][j] += region_avg
                            count_regions[i][j] += 1

        for i in range(m):
            for j in range(n):
                if count_regions[i][j] > 0:
                    result[i][j] = sum_region_averages[i][j] // count_regions[i][j]
                
        return result

```