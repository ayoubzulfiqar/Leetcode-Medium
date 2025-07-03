class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_counts = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            remainder = (current_sum % k + k) % k
            
            count += remainder_counts.get(remainder, 0)
            
            remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
            
        return count