class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        n = len(nums)
        
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            inner_expression = "/".join(str(num) for num in nums[1:])
            return str(nums[0]) + "/(" + inner_expression + ")"