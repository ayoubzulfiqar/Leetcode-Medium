class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        
        freq = [0] * 101 
        for num in arr:
            freq[num] += 1
        
        ans = 0
        
        for x in range(101):
            if freq[x] == 0:
                continue
            
            for y in range(x, 101):
                if freq[y] == 0:
                    continue
                
                z = target - x - y
                
                if z < y or z > 100:
                    continue
                
                if freq[z] == 0:
                    continue
                
                if x == y == z:
                    if freq[x] >= 3:
                        ans = (ans + (freq[x] * (freq[x] - 1) * (freq[x] - 2) // 6)) % MOD
                elif x == y:
                    if freq[x] >= 2:
                        ans = (ans + (freq[x] * (freq[x] - 1) // 2) * freq[z]) % MOD
                elif y == z:
                    if freq[y] >= 2:
                        ans = (ans + freq[x] * (freq[y] * (freq[y] - 1) // 2)) % MOD
                else: # x < y < z
                    ans = (ans + freq[x] * freq[y] * freq[z]) % MOD
                    
        return ans