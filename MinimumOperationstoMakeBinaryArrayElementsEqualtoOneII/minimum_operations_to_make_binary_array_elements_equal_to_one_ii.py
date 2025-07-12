class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        current_flip_state = 0 

        for i in range(len(nums)):
            if (nums[i] + current_flip_state) % 2 == 0:
                operations += 1
                current_flip_state = 1 - current_flip_state
        
        return operations