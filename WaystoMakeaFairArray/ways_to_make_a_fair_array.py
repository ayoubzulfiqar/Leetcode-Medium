class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefix_even = [0] * n
        prefix_odd = [0] * n

        for k in range(n):
            if k > 0:
                prefix_even[k] = prefix_even[k-1]
                prefix_odd[k] = prefix_odd[k-1]
            
            if k % 2 == 0:
                prefix_even[k] += nums[k]
            else:
                prefix_odd[k] += nums[k]

        total_even_sum = prefix_even[n-1]
        total_odd_sum = prefix_odd[n-1]

        count = 0
        for i in range(n):
            left_even_sum = prefix_even[i-1] if i > 0 else 0
            left_odd_sum = prefix_odd[i-1] if i > 0 else 0

            right_even_orig_idx_sum = total_even_sum - prefix_even[i]
            right_odd_orig_idx_sum = total_odd_sum - prefix_odd[i]

            new_even_sum = left_even_sum + right_odd_orig_idx_sum
            new_odd_sum = left_odd_sum + right_even_orig_idx_sum

            if new_even_sum == new_odd_sum:
                count += 1
        
        return count