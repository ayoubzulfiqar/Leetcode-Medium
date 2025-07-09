class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count = 0
        last_kept = -1

        for num in nums:
            if count % 2 == 0:
                last_kept = num
                count += 1
            else:
                if num != last_kept:
                    count += 1
        
        deletions = len(nums) - count
        
        if count % 2 != 0:
            deletions += 1
            
        return deletions