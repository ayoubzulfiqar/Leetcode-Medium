class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        current_prefix_sum = 0
        count_even = 1
        count_odd = 0
        total_odd_subarrays = 0
        
        for num in arr:
            current_prefix_sum += num
            
            if current_prefix_sum % 2 == 1:
                total_odd_subarrays = (total_odd_subarrays + count_even) % MOD
                count_odd += 1
            else:
                total_odd_subarrays = (total_odd_subarrays + count_odd) % MOD
                count_even += 1
                
        return total_odd_subarrays