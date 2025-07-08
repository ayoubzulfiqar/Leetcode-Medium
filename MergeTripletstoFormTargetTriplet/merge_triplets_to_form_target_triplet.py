class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        res = [0, 0, 0]
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                res[0] = max(res[0], t[0])
                res[1] = max(res[1], t[1])
                res[2] = max(res[2], t[2])
        
        return res == target