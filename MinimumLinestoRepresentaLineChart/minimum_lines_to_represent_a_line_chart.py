class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        n = len(stockPrices)

        if n <= 1:
            return 0
        if n == 2:
            return 1

        stockPrices.sort()

        lines = 1

        for i in range(2, n):
            x1, y1 = stockPrices[i-2]
            x2, y2 = stockPrices[i-1]
            x3, y3 = stockPrices[i]

            # Check collinearity using the cross-product method:
            # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
            # If this equality does not hold, the three points are not collinear,
            # meaning a new line segment starts from stockPrices[i-1].
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                lines += 1
        
        return lines