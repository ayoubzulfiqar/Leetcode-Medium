import math

class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        bad_numbers = set()
        n = len(fronts)

        for i in range(n):
            if fronts[i] == backs[i]:
                bad_numbers.add(fronts[i])
        
        min_good_val = math.inf
        
        for val in fronts:
            if val not in bad_numbers:
                min_good_val = min(min_good_val, val)
        
        for val in backs:
            if val not in bad_numbers:
                min_good_val = min(min_good_val, val)
        
        if min_good_val == math.inf:
            return 0
        else:
            return int(min_good_val)