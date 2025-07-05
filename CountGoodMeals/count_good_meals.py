import collections

class Solution:
    def countGoodMeals(self, deliciousness: list[int]) -> int:
        MOD = 10**9 + 7
        
        powers_of_two = [1 << i for i in range(22)] 
        
        freq = collections.defaultdict(int)
        ans = 0
        
        for x in deliciousness:
            for p in powers_of_two:
                complement = p - x
                if complement in freq:
                    ans = (ans + freq[complement]) % MOD
            
            freq[x] += 1
            
        return ans