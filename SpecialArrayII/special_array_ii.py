class Solution:
    def checkSpecialArray(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        
        prefix_violations = [0] * n
        
        for i in range(n - 1):
            if (nums[i] % 2) == (nums[i+1] % 2):
                prefix_violations[i+1] = prefix_violations[i] + 1
            else:
                prefix_violations[i+1] = prefix_violations[i]
        
        results = []
        for fromi, toi in queries:
            num_violations_in_range = prefix_violations[toi] - prefix_violations[fromi]
            
            if num_violations_in_range == 0:
                results.append(True)
            else:
                results.append(False)
                
        return results