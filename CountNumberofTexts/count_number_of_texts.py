class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        
        MAX_BLOCK_LEN = 100000 

        dp3 = [0] * (MAX_BLOCK_LEN + 1)
        dp3[0] = 1 
        dp3[1] = 1 
        dp3[2] = 2 
        dp3[3] = 4 
        
        for i in range(4, MAX_BLOCK_LEN + 1):
            dp3[i] = (dp3[i-1] + dp3[i-2] + dp3[i-3]) % MOD

        dp4 = [0] * (MAX_BLOCK_LEN + 1)
        dp4[0] = 1 
        dp4[1] = 1 
        dp4[2] = 2 
        dp4[3] = 4 
        dp4[4] = 8 

        for i in range(5, MAX_BLOCK_LEN + 1):
            dp4[i] = (dp4[i-1] + dp4[i-2] + dp4[i-3] + dp4[i-4]) % MOD

        total_ways = 1
        n = len(pressedKeys)
        i = 0
        while i < n:
            current_char = pressedKeys[i]
            count = 0
            j = i
            while j < n and pressedKeys[j] == current_char:
                count += 1
                j += 1
            
            if current_char == '7' or current_char == '9':
                ways_for_block = dp4[count]
            else: 
                ways_for_block = dp3[count]
            
            total_ways = (total_ways * ways_for_block) % MOD
            
            i = j 
        
        return total_ways