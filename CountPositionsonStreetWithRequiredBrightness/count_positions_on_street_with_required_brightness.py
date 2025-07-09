class Solution:
    def countPositions(self, n: int, lights: list[list[int]], requirement: list[int]) -> int:
        brightness_diff = [0] * (n + 1)

        for pos, r in lights:
            start_idx = max(0, pos - r)
            end_idx = min(n - 1, pos + r)
            
            brightness_diff[start_idx] += 1
            if end_idx + 1 < n + 1:
                brightness_diff[end_idx + 1] -= 1
        
        actual_brightness = [0] * n
        current_brightness = 0
        for i in range(n):
            current_brightness += brightness_diff[i]
            actual_brightness[i] = current_brightness
            
        count = 0
        for i in range(n):
            if actual_brightness[i] >= requirement[i]:
                count += 1
                
        return count