class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]
        
        total_sum = prefix_sums[n]
        
        result = [0] * n
        
        for i in range(n):
            current_num = nums[i]
            
            # Sum for elements to the left: sum(nums[i] - nums[j]) for j < i
            # This is i * nums[i] - (sum of nums[0] to nums[i-1])
            sum_left_diffs = i * current_num - prefix_sums[i]
            
            # Sum for elements to the right: sum(nums[j] - nums[i]) for j > i
            # This is (sum of nums[i+1] to nums[n-1]) - (count of elements to the right) * nums[i]
            # The sum of elements to the right is total_sum - prefix_sums[i+1]
            # The count of elements to the right is (n - 1 - i)
            sum_right_diffs = (total_sum - prefix_sums[i+1]) - (n - 1 - i) * current_num
            
            result[i] = sum_left_diffs + sum_right_diffs
            
        return result