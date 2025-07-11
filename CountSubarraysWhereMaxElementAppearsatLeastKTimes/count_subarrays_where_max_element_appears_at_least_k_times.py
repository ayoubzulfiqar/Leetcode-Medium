class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_val = max(nums)
        
        def count_at_most_k_times(k_limit: int) -> int:
            n = len(nums)
            left = 0
            current_max_val_count = 0
            subarrays_count = 0
            
            for right in range(n):
                if nums[right] == max_val:
                    current_max_val_count += 1
                
                while current_max_val_count > k_limit:
                    if nums[left] == max_val:
                        current_max_val_count -= 1
                    left += 1
                
                subarrays_count += (right - left + 1)
            
            return subarrays_count

        return count_at_most_k_times(len(nums)) - count_at_most_k_times(k - 1)