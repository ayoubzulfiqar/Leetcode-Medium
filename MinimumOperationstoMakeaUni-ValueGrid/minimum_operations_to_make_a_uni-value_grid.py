class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        nums = []
        for r in range(m):
            for c in range(n):
                nums.append(grid[r][c])
        
        if not nums:
            return 0
        
        first_remainder = nums[0] % x
        for i in range(1, len(nums)):
            if nums[i] % x != first_remainder:
                return -1
        
        nums.sort()
        
        median_val = nums[len(nums) // 2]
        
        total_operations = 0
        for num in nums:
            total_operations += abs(num - median_val) // x
            
        return total_operations