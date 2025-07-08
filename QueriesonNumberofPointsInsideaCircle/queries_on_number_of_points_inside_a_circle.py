class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        answer = []
        for qx, qy, qr in queries:
            count = 0
            qr_squared = qr * qr
            for px, py in points:
                dx = px - qx
                dy = py - qy
                distance_squared = dx * dx + dy * dy
                if distance_squared <= qr_squared:
                    count += 1
            answer.append(count)
        return answer