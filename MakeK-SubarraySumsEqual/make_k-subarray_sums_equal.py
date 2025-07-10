import math

class Solution:
    def makeKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        g = math.gcd(n, k)
        
        total_operations = 0
        
        for start_idx in range(g):
            current_group_elements = []
            
            current_ptr = start_idx
            for _ in range(n // g):
                current_group_elements.append(arr[current_ptr])
                current_ptr = (current_ptr + k) % n
            
            current_group_elements.sort()
            
            median = current_group_elements[len(current_group_elements) // 2]
            
            for val in current_group_elements:
                total_operations += abs(val - median)
                
        return total_operations