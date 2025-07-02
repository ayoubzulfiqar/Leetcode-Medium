class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        stack = [] 

        for i in range(2 * n - 1, -1, -1):
            idx = i % n
            current_val = nums[idx]

            while stack and stack[-1] <= current_val:
                stack.pop()

            if stack:
                ans[idx] = stack[-1]
            
            stack.append(current_val)
        
        return ans