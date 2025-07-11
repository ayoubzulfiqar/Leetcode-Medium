class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        indices_a = []
        idx = s.find(a, 0)
        while idx != -1:
            indices_a.append(idx)
            idx = s.find(a, idx + 1)

        indices_b = []
        idx = s.find(b, 0)
        while idx != -1:
            indices_b.append(idx)
            idx = s.find(b, idx + 1)

        beautiful_indices = []
        
        p_b = 0 

        for i in indices_a:
            while p_b < len(indices_b) and indices_b[p_b] < i - k:
                p_b += 1
            
            if p_b < len(indices_b) and indices_b[p_b] <= i + k:
                beautiful_indices.append(i)
                
        return beautiful_indices