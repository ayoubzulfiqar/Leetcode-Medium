class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        results = []
        current_subset = []
        
        nums.sort()
        
        def backtrack(start_index):
            results.append(list(current_subset))
            
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                
                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()
        
        backtrack(0)
        return results