import bisect

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        starts_with_original_indices = []
        for i in range(n):
            starts_with_original_indices.append((intervals[i][0], i))
            
        starts_with_original_indices.sort()
        
        start_values = [item[0] for item in starts_with_original_indices]
        
        result = [-1] * n
        
        for i in range(n):
            current_end = intervals[i][1]
            
            idx = bisect.bisect_left(start_values, current_end)
            
            if idx < n:
                result[i] = starts_with_original_indices[idx][1]
                
        return result