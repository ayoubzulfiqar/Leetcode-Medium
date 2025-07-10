import collections

class Solution:
    def sumOfDistancesInArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [0] * n
        
        val_to_indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            val_to_indices[num].append(i)
            
        for indices_list in val_to_indices.values():
            k = len(indices_list)
            if k <= 1:
                continue
            
            ps = [0] * (k + 1)
            for x in range(k):
                ps[x+1] = ps[x] + indices_list[x]
            
            for m in range(k):
                current_idx = indices_list[m]
                
                count_left = m
                S_left = ps[m]
                
                count_right = k - 1 - m
                S_right = ps[k] - ps[m+1]
                
                term_left = count_left * current_idx - S_left
                term_right = S_right - count_right * current_idx
                
                arr[current_idx] = term_left + term_right
                
        return arr