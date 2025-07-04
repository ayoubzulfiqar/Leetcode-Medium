class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        distX = xCenter - closestX
        distY = yCenter - closestY

        distanceSquared = (distX * distX) + (distY * distY)

        return distanceSquared <= (radius * radius)