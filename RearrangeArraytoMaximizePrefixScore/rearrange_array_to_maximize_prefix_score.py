class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        
        score = 0
        current_prefix_sum = 0
        
        for num in nums:
            current_prefix_sum += num
            if current_prefix_sum > 0:
                score += 1
            else:
                break
                
        return score