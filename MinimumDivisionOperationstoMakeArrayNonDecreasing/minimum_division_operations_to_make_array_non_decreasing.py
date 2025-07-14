class Solution:
    def minOperations(self, nums: list[int]) -> int:
        MAX_VAL = 10**6
        
        spf = list(range(MAX_VAL + 1))
        spf[0] = 0
        spf[1] = 1 

        primes = []
        for i in range(2, MAX_VAL + 1):
            if spf[i] == i:
                primes.append(i)
            
            for p in primes:
                if p > spf[i] or i * p > MAX_VAL:
                    break
                spf[i * p] = p

        operations = 0
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            current_val = nums[i]
            next_val = nums[i+1]
            
            if current_val <= next_val:
                continue
            
            operations += 1
            
            new_current_val = spf[current_val]
            
            if new_current_val > next_val:
                return -1
            
            nums[i] = new_current_val
            
        return operations