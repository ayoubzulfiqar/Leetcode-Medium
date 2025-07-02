class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp_len = [1] * n
        dp_prev = [-1] * n

        max_len = 0
        end_idx = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp_len[j] + 1 > dp_len[i]:
                        dp_len[i] = dp_len[j] + 1
                        dp_prev[i] = j
            
            if dp_len[i] > max_len:
                max_len = dp_len[i]
                end_idx = i
        
        result = []
        current_idx = end_idx
        while current_idx != -1:
            result.append(nums[current_idx])
            current_idx = dp_prev[current_idx]
        
        return result[::-1]