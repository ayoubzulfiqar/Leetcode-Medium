import math

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        n = len(nums)
        
        min_val_candidate = math.inf
        min_idx_candidate = -1
        
        max_val_candidate = -math.inf
        max_idx_candidate = -1
        
        for i in range(n):
            if i - indexDifference >= 0:
                current_k_idx = i - indexDifference
                
                if nums[current_k_idx] < min_val_candidate:
                    min_val_candidate = nums[current_k_idx]
                    min_idx_candidate = current_k_idx
                
                if nums[current_k_idx] > max_val_candidate:
                    max_val_candidate = nums[current_k_idx]
                    max_idx_candidate = current_k_idx
            
            if min_idx_candidate != -1 and abs(nums[i] - min_val_candidate) >= valueDifference:
                return [min_idx_candidate, i]
            
            if max_idx_candidate != -1 and abs(nums[i] - max_val_candidate) >= valueDifference:
                return [max_idx_candidate, i]
                
        return [-1, -1]