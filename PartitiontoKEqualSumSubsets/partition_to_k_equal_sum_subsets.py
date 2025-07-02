class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        
        if any(num > target_sum for num in nums):
            return False
            
        nums.sort(reverse=True)
        
        n = len(nums)
        
        memo = {}
        
        def backtrack(mask: int, current_bucket_sum: int, buckets_formed: int) -> bool:
            if buckets_formed == k:
                return True
            
            if (mask, buckets_formed) in memo:
                return memo[(mask, buckets_formed)]
            
            if current_bucket_sum == target_sum:
                res = backtrack(mask, 0, buckets_formed + 1)
                memo[(mask, buckets_formed)] = res
                return res
            
            for i in range(n):
                if (mask >> i) & 1:
                    continue
                
                if current_bucket_sum + nums[i] <= target_sum:
                    new_mask = mask | (1 << i)
                    
                    if backtrack(new_mask, current_bucket_sum + nums[i], buckets_formed):
                        memo[(mask, buckets_formed)] = True
                        return True
            
            memo[(mask, buckets_formed)] = False
            return False

        return backtrack(0, 0, 0)