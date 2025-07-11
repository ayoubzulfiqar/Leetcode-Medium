class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_length = 0
        left = 0
        freq = {}

        for right in range(n):
            num_right = nums[right]
            freq[num_right] = freq.get(num_right, 0) + 1

            while freq[num_right] > k:
                num_left = nums[left]
                freq[num_left] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length