class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
            
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
            
        for k in range(1, n):
            if prefix_max[k-1] <= suffix_min[k]:
                return k
        
        # According to the problem constraints, a valid partition always exists,
        # so this line should theoretically not be reached.
        return -1