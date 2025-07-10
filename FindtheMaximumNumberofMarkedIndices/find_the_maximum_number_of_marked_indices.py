class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        i = 0
        j = n // 2
        
        marked_pairs_count = 0
        
        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                marked_pairs_count += 1
                i += 1
                j += 1
            else:
                j += 1
                
        return 2 * marked_pairs_count