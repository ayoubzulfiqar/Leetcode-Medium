class Solution:
    def numOfSubsequencesWithOddSum(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        even_count = 0
        odd_count = 0
        
        for num in arr:
            if num % 2 == 0:
                prev_even_count = even_count
                prev_odd_count = odd_count
                
                even_count = (prev_even_count + prev_even_count + 1) % MOD
                odd_count = (prev_odd_count + prev_odd_count) % MOD
                
            else:
                prev_even_count = even_count
                prev_odd_count = odd_count
                
                even_count = (prev_even_count + prev_odd_count) % MOD
                odd_count = (prev_odd_count + prev_even_count + 1) % MOD
        
        return odd_count