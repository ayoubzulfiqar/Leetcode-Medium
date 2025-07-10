class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        
        final_positions = []
        for i in range(n):
            if s[i] == 'R':
                final_positions.append(nums[i] + d)
            else:
                final_positions.append(nums[i] - d)
        
        final_positions.sort()
        
        total_distance = 0
        for k in range(n):
            coefficient = (2 * k - n + 1)
            term = coefficient * final_positions[k]
            total_distance = (total_distance + term) % MOD
            
        return total_distance