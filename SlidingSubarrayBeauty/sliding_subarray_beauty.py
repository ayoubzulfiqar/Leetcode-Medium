class Solution:
    def beautifulSubarrays(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        results = []
        
        counts = [0] * 101 
        
        def calculate_beauty():
            neg_count = 0
            for i in range(50):
                neg_count += counts[i]
                if neg_count >= x:
                    return i - 50
            return 0
            
        for i in range(k):
            counts[nums[i] + 50] += 1
        
        results.append(calculate_beauty())
        
        for i in range(k, n):
            counts[nums[i - k] + 50] -= 1
            counts[nums[i] + 50] += 1
            
            results.append(calculate_beauty())
            
        return results