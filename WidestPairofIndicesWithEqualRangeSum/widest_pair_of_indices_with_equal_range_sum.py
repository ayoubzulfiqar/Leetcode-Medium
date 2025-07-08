class Solution:
    def widestPairOfIndicesWithEqualRangeSum(self, nums: list[int]) -> int:
        sum_to_first_index = {0: -1}
        current_sum = 0
        max_width = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if current_sum in sum_to_first_index:
                first_occurrence_index = sum_to_first_index[current_sum]
                max_width = max(max_width, i - first_occurrence_index)
            else:
                sum_to_first_index[current_sum] = i
                
        return max_width