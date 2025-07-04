import collections

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_deque = collections.deque()
        max_deque = collections.deque()
        
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len