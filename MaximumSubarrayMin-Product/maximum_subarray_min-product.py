class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        left_boundary = [0] * n
        stack = [] 
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if not stack:
                left_boundary[i] = 0
            else:
                left_boundary[i] = stack[-1] + 1
            stack.append(i)

        right_boundary = [0] * n
        stack = [] 
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if not stack:
                right_boundary[i] = n - 1
            else:
                right_boundary[i] = stack[-1] - 1
            stack.append(i)
        
        max_product = 0
        for i in range(n):
            L = left_boundary[i]
            R = right_boundary[i]
            
            current_sum = prefix_sum[R+1] - prefix_sum[L]
            current_product = nums[i] * current_sum
            
            if current_product > max_product:
                max_product = current_product
        
        return max_product % MOD