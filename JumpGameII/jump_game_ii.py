class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_reach = 0
        max_reach = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == current_reach:
                jumps += 1
                current_reach = max_reach
                
                if current_reach >= n - 1:
                    break

        return jumps