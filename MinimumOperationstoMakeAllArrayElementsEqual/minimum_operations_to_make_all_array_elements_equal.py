import bisect

class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        results = []
        for q in queries:
            k = bisect.bisect_right(nums, q)
            
            sum_le_q = prefix_sum[k]
            count_le_q = k
            
            sum_gt_q = prefix_sum[n] - prefix_sum[k]
            count_gt_q = n - k
            
            ops_le_q = count_le_q * q - sum_le_q
            ops_gt_q = sum_gt_q - count_gt_q * q
            
            total_ops = ops_le_q + ops_gt_q
            results.append(total_ops)
            
        return results