import collections

class Solution:
    def distinctColors(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_colors = {}
        color_frequencies = collections.defaultdict(int)
        
        result = []
        
        for ball, new_color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                
                color_frequencies[old_color] -= 1
                
                if color_frequencies[old_color] == 0:
                    del color_frequencies[old_color]
            
            ball_colors[ball] = new_color
            
            color_frequencies[new_color] += 1
            
            result.append(len(color_frequencies))
            
        return result