class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        zeros_left = 0
        ones_right = sum(nums)
        
        max_score = -1
        result_indices = []
        
        for i in range(n + 1):
            current_score = zeros_left + ones_right
            
            if current_score > max_score:
                max_score = current_score
                result_indices = [i]
            elif current_score == max_score:
                result_indices.append(i)
            
            if i < n:
                if nums[i] == 0:
                    zeros_left += 1
                else:
                    ones_right -= 1
                    
        return result_indices