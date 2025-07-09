import collections

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        freq = collections.Counter()
        
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            freq[nums[right]] += 1
            
            if right - left + 1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, current_sum)
                
                current_sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
                
        return max_sum