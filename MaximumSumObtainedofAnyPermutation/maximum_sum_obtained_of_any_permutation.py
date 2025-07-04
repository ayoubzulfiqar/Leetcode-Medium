class Solution:
    def maxTotalSum(self, nums: list[int], requests: list[list[int]]) -> int:
        n = len(nums)
        
        counts = [0] * n
        for start, end in requests:
            counts[start] += 1
            if end + 1 < n:
                counts[end + 1] -= 1
        
        current_frequency = 0
        for i in range(n):
            current_frequency += counts[i]
            counts[i] = current_frequency
            
        nums.sort(reverse=True)
        counts.sort(reverse=True)
        
        total_sum = 0
        MOD = 10**9 + 7
        
        for i in range(n):
            total_sum = (total_sum + nums[i] * counts[i]) % MOD
            
        return total_sum

# Example Usage (for testing, not part of the required output)
# sol = Solution()
# print(sol.maxTotalSum(nums = [1,2,3,4,5], requests = [[1,3],[0,1]])) # Output: 19
# print(sol.maxTotalSum(nums = [1,2,3,4,5,6], requests = [[0,1]])) # Output: 11
# print(sol.maxTotalSum(nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]])) # Output: 47