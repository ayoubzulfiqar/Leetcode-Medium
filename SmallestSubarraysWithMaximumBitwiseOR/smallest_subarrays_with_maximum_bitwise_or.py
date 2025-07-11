class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        overall_max_or = 0
        for x in nums:
            overall_max_or |= x
            
        answer = [0] * n
        
        bit_counts = [0] * 32
        
        right = 0
        current_or = 0
        
        for left in range(n):
            while right < n and current_or != overall_max_or:
                num_to_add = nums[right]
                for k in range(32):
                    if (num_to_add >> k) & 1:
                        bit_counts[k] += 1
                current_or |= num_to_add
                right += 1
            
            answer[left] = right - left
            
            num_to_remove = nums[left]
            for k in range(32):
                if (num_to_remove >> k) & 1:
                    bit_counts[k] -= 1
                    if bit_counts[k] == 0:
                        current_or &= ~(1 << k)
                        
        return answer