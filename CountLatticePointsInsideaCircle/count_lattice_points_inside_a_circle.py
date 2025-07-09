class Solution:
    def countPoints(self, circles: list[list[int]]) -> int:
        lattice_points = set()
        
        for px in range(0, 201):
            for py in range(0, 201):
                for cx, cy, r in circles:
                    dist_sq = (px - cx)**2 + (py - cy)**2
                    r_sq = r**2
                    if dist_sq <= r_sq:
                        lattice_points.add((px, py))
                        break
        
        return len(lattice_points)