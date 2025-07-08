class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        
        current_max_val = 1 
        
        for i in range(1, len(arr)):
            current_max_val = min(arr[i], current_max_val + 1)
            
        return current_max_val