import collections

class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total_count = 0
        left = 0
        
        min_deque = collections.deque()
        max_deque = collections.deque()
        
        for right in range(n):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            total_count += (right - left + 1)
            
        return total_count