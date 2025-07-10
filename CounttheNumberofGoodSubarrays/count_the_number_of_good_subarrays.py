import collections

class Solution:
    def numberOfGoodSubarrays(self, nums: list[int], k: int) -> int:
        count_good_subarrays = 0
        left = 0
        current_pairs = 0
        freq = collections.Counter()

        for right in range(len(nums)):
            num_r = nums[right]
            
            current_pairs += freq[num_r] 
            freq[num_r] += 1

            while current_pairs >= k:
                count_good_subarrays += (len(nums) - right)
                
                num_l = nums[left]
                
                freq[num_l] -= 1
                current_pairs -= freq[num_l]
                
                left += 1
                
        return count_good_subarrays