class Solution:
    def findPowerOfKSizeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            is_valid_power = True
            
            if k == 1:
                results.append(nums[i])
                continue

            first_val = nums[i]
            for j in range(1, k):
                if nums[i + j] != first_val + j:
                    is_valid_power = False
                    break
            
            if is_valid_power:
                results.append(nums[i + k - 1])
            else:
                results.append(-1)
                
        return results