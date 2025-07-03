class CustomFunction:
    def f(self, x: int, y: int) -> int:
        pass

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> list[list[int]]:
        results = []
        x = 1
        y = 1000

        while x <= 1000 and y >= 1:
            current_val = customfunction.f(x, y)
            if current_val == z:
                results.append([x, y])
                x += 1
                y -= 1
            elif current_val < z:
                x += 1
            else:
                y -= 1
        
        return results