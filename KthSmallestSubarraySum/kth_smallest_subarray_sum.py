class Solution:
    def kthSmallestSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Calculate prefix sums
        # prefix_sum[i] stores the sum of nums[0]...nums[i-1]
        # prefix_sum[0] = 0
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        # Generate all subarray sums
        subarray_sums = []
        for i in range(n):
            for j in range(i, n):
                # Sum of subarray nums[i...j] is prefix_sum[j+1] - prefix_sum[i]
                subarray_sums.append(prefix_sum[j+1] - prefix_sum[i])
                
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Return the k-th smallest sum (0-indexed k-1)
        return subarray_sums[k-1]