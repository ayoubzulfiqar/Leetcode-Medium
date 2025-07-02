class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        s3_val = -float('inf') 
        stack = [] 

        for k_idx in range(n - 1, -1, -1):
            current_num = nums[k_idx]

            if current_num < s3_val:
                return True

            while stack and current_num > stack[-1]:
                s3_val = stack.pop()

            stack.append(current_num)

        return False