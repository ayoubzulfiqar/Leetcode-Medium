import collections

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)

        counts = collections.Counter(nums)
        
        dominant_val = -1
        total_dominant_count = 0
        for val, count in counts.items():
            if count * 2 > n:
                dominant_val = val
                total_dominant_count = count
                break
        
        left_dominant_count = 0
        for i in range(n - 1):
            if nums[i] == dominant_val:
                left_dominant_count += 1
            
            left_len = i + 1
            right_len = n - left_len
            
            right_dominant_count = total_dominant_count - left_dominant_count
            
            is_left_dominant = (left_dominant_count * 2 > left_len)
            is_right_dominant = (right_dominant_count * 2 > right_len)
            
            if is_left_dominant and is_right_dominant:
                return i
        
        return -1