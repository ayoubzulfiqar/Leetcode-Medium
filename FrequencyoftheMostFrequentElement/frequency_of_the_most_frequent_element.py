class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        
        left = 0
        current_sum = 0
        max_freq = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # The cost to make all elements in the window [left, right] equal to nums[right]
            # is (length of window * nums[right]) - sum of elements in window
            # If this cost exceeds k, shrink the window from the left
            while (right - left + 1) * nums[right] - current_sum > k:
                current_sum -= nums[left]
                left += 1
            
            # The current window is valid, update max_freq
            max_freq = max(max_freq, right - left + 1)
            
        return max_freq